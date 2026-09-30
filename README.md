# Expeditions map making guide

A plain-language guide to building custom maps for *Expeditions: A MudRunner Game*.

Saber's official guides are accurate and organised field by field, in the order the
software stores things. This guide explains what a thing is and what it is for
before it tells you which boxes to fill in.

Not affiliated with or endorsed by Saber Interactive.

## Reading it

The built site lives in `docs/` and is what GitHub Pages serves.

## Editing it

Content is markdown in `content/`. One file per page, with YAML front matter:

```yaml
---
title: Roads are not carved terrain
part: The land
order: 230
summary: One sentence. Used on cards and in search results.
status: outline      # omit when the page is finished
---
```

- `part` groups pages into a sidebar section. Sections appear in the order their
  first page appears.
- `order` sorts every page globally. Leave gaps so pages can be inserted later.
- `status` marks a page unfinished. Anything other than `done` shows a banner on
  the page and a label in the sidebar. Omit it when the page is complete.
- A front matter value containing `": "` **must be quoted**, or YAML reads it as a
  nested mapping.

Then:

```
python build.py            # build into docs/
python build.py --serve    # build, then preview at http://127.0.0.1:8137
```

Requires `markdown`, `pyyaml`, `jinja2` and `pygments`.

## Publishing

GitHub Pages is configured to serve `/docs` from `main`, so there is no Actions
workflow and no Jekyll step. Build, commit, push.

```
python build.py
git add -A && git commit -m "..." && git push
```

## How claims are labelled

Modding an engine you did not write means some things are documented, some are
discovered by reading the shipped files, and some are still inference. Pages label
which is which wherever it matters:

- **documented** stated in Saber's official guides
- **schema only** present in the editor's own type definitions and in the shipped
  game code, but absent from the official guides
- **unverified** worked out from evidence, not yet proven in a running game

Write the label in the markdown as inline HTML:

```html
<span class="prov prov-doc">documented</span>
<span class="prov prov-schema">schema only</span>
<span class="prov prov-unver">unverified</span>
```

Never promote an inference to a fact to make a page look finished. A page that says
"unverified" is more useful than one that is quietly wrong.

## Callouts

Standard python-markdown admonitions, styled by severity:

```
!!! danger "Crashes the game"
!!! warning "Fails silently"
!!! tip "Do it this way"
```

## Contributing

Corrections are the most valuable contribution, especially:

- anything marked **unverified** that you have actually tested
- the three undocumented assignment types, if you get one working
- `blockerObjectives`, which the guides call absent but the schema only hides

If you tested something and it behaved differently, that is worth an issue even
without an explanation.
