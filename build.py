#!/usr/bin/env python3
"""Build the static guide site into docs/ for GitHub Pages.

No build step for the reader and no Actions workflow: GitHub Pages can serve
`/docs` on `main` directly, so `python build.py` then `git push` publishes.

    python build.py            # build into docs/
    python build.py --serve    # build, then preview at http://127.0.0.1:8137

Content lives in `content/` as markdown with YAML front matter:

    ---
    title: Your first map
    part: Getting started
    order: 120
    summary: One sentence for the card and the search result.
    status: draft          # optional; anything other than 'done' shows a banner
    ---

`part` groups pages in the sidebar, `order` sorts them globally (so pick
numbers with gaps). Everything else is derived.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys

try:
    import markdown
    import yaml
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError as e:  # pragma: no cover
    raise SystemExit(f"missing dependency: {e.name}. pip install markdown pyyaml jinja2 pygments")

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "docs")
TEMPLATES = os.path.join(ROOT, "templates")
ASSETS = os.path.join(ROOT, "assets")

MD_EXT = ["extra", "admonition", "toc", "sane_lists", "smarty", "codehilite"]
MD_CFG = {
    "codehilite": {"css_class": "hl", "guess_lang": False},
    "toc": {"permalink": "#", "toc_depth": "2-3"},
    "smarty": {"smart_dashes": False},   # never silently turn -- into an en dash
}


def split_front_matter(text: str, where: str = "?"):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    try:
        meta = yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError as e:
        # by far the usual cause is a value containing ": ", which YAML reads as
        # a nested mapping. Name the file, because a bare traceback does not.
        raise SystemExit(f"front matter is not valid YAML in {where}:\n  {e}\n"
                         '  a value containing ": " must be wrapped in quotes')
    return meta, text[end + 4:].lstrip("\n")


def slug_for(path: str) -> str:
    """content/01-land/roads.md -> 01-land/roads.html, index.md -> index.html"""
    rel = os.path.relpath(path, CONTENT).replace(os.sep, "/")
    return re.sub(r"\.md$", ".html", rel)


def strip_html(s: str) -> str:
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def collect():
    pages = []
    for base, _dirs, files in os.walk(CONTENT):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            p = os.path.join(base, f)
            meta, body = split_front_matter(open(p, encoding="utf-8").read(), os.path.relpath(p, ROOT))
            if not meta.get("title"):
                print(f"   ! {os.path.relpath(p, ROOT)} has no title, skipped")
                continue
            md = markdown.Markdown(extensions=MD_EXT, extension_configs=MD_CFG)
            rendered = md.convert(body)
            pages.append(dict(
                meta=meta,
                title=meta["title"],
                part=meta.get("part", "Reference"),
                order=int(meta.get("order", 9999)),
                summary=meta.get("summary", ""),
                status=meta.get("status", "done"),
                url=slug_for(p),
                depth=slug_for(p).count("/"),
                html=rendered,
                toc=getattr(md, "toc", ""),
                text=strip_html(rendered),
                src=os.path.relpath(p, ROOT).replace(os.sep, "/"),
            ))
    pages.sort(key=lambda x: (x["order"], x["title"]))
    return pages


def nav_for(pages):
    """Sidebar structure: ordered parts, each with its ordered pages."""
    parts, seen = [], {}
    for p in pages:
        if p["url"] == "index.html":
            continue
        if p["part"] not in seen:
            seen[p["part"]] = {"name": p["part"], "pages": []}
            parts.append(seen[p["part"]])
        seen[p["part"]]["pages"].append(p)
    return parts


def build(serve: bool) -> int:
    if not os.path.isdir(CONTENT):
        raise SystemExit(f"no content directory at {CONTENT}")
    pages = collect()
    if not pages:
        raise SystemExit("no pages found")
    parts = nav_for(pages)

    env = Environment(loader=FileSystemLoader(TEMPLATES),
                      autoescape=select_autoescape(["html"]),
                      trim_blocks=True, lstrip_blocks=True)
    tpl = env.get_template("page.html")

    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        q = os.path.join(OUT, name)
        if name == "CNAME":
            continue
        shutil.rmtree(q) if os.path.isdir(q) else os.remove(q)

    # assets, verbatim
    if os.path.isdir(ASSETS):
        shutil.copytree(ASSETS, os.path.join(OUT, "assets"))

    # GitHub Pages would otherwise run Jekyll over this and drop _underscore dirs
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    index = []
    drafts = []
    for i, p in enumerate(pages):
        prevp = pages[i - 1] if i > 0 else None
        nextp = pages[i + 1] if i + 1 < len(pages) else None
        # every page sits at the same depth or deeper, so resolve links to root
        up = "../" * p["depth"]
        out_path = os.path.join(OUT, p["url"])
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        open(out_path, "w", encoding="utf-8").write(tpl.render(
            page=p, parts=parts, root=up, prev=prevp, next=nextp,
            is_home=(p["url"] == "index.html"),
        ))
        index.append({"t": p["title"], "u": p["url"], "p": p["part"],
                      "s": p["summary"], "x": p["text"][:1800]})
        if p["status"] != "done":
            drafts.append(p)

    json.dump(index, open(os.path.join(OUT, "search.json"), "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"))

    print(f"built {len(pages)} page(s) into docs/  ({len(parts)} parts)")
    for part in parts:
        print(f"   {part['name']}")
        for p in part["pages"]:
            flag = "" if p["status"] == "done" else f"   [{p['status']}]"
            print(f"      {p['order']:>4}  {p['title']}{flag}")
    if drafts:
        print(f"\n{len(drafts)} page(s) not marked done:")
        for p in drafts:
            print(f"   {p['status']:<10} {p['src']}")

    if serve:
        import functools
        import http.server
        import socketserver
        import subprocess
        h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=OUT)
        with socketserver.TCPServer(("127.0.0.1", 8137), h) as srv:
            print("\npreview at http://127.0.0.1:8137  (ctrl-c to stop)")
            try:
                srv.serve_forever()
            except KeyboardInterrupt:
                print("\nstopped")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--serve", action="store_true", help="preview after building")
    return build(ap.parse_args().serve)


if __name__ == "__main__":
    raise SystemExit(main())
