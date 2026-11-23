---
title: Breakable fences and guardrails from a line
part: Dressing the map
order: 325
status: draft
summary: Lay a fence or guardrail like a road, then let the Fence Lines app turn it into sections trucks can knock down.
---

A fence or guardrail can go on a map two ways, and each has a catch. **As a line** (an
overlay, drawn like a road), it follows your curve and the ground, but it never breaks:
a truck stops dead against it. **As models** placed one section at a time, it breaks,
but a long run means placing and lining up every section by hand.

**Fence Lines** gives you both. You draw the line, and the app replaces it with
breakable sections that follow the same path.

!!! note "How much of this is tested"
    Breakable fence sections have been knocked down **in a running game**. The app's
    placement has been checked against saved maps, and the sections it writes have passed
    the game's converter. The finished runs have not yet been looked at in the editor or
    driven into in a game. See [What is not known yet](#what-is-not-known-yet).

## Why a line can't break

The game breaks a model by its parts. A breakable fence section is built from separate
pieces (a first post, the panel or rail, a far post), each held to the next by a joint
with a breaking strength. A hard enough hit snaps the joint and the piece falls. The
game's own breakable fences work the same way.

An overlay is one mesh stretched along your line and pressed onto the ground. It has
collision, so it stops a truck, but it has no parts and no joints, so nothing on it can
come loose. No setting in its files changes that. To make a line breakable, it has to
be swapped for models.

## What you need

- The **Fences** or **Guardrails** package installed whole. Each one installs the
  Fence Lines app (Start menu) along with the pieces it places. A line whose pieces
  are missing is skipped, with a message naming them.

| Line | Becomes |
|---|---|
| Any of the 11 fence lines (`fence_..._line`) | Breakable fence sections, a post at every joint and at both ends |
| `guardrail_line` (steel W-beam) | Breakable rail sections with a steel end cap on each end |
| `guardrail_timber_line` | Breakable timber rail with the turned-down timber end on each end |
| `guardrail_log_line` | Breakable log rail with the sloping log end on each end |
| The two stone wall lines | Left as lines: stone is built not to break |

## Making a line breakable

1. Draw the line in the editor, from the **overlay** list, the way you would draw a road.
   You can draw as many lines as you like, in any styles, on any of your maps.
2. **Save** the map.
3. **Close the editor.** The editor keeps the map in memory, and a save after the app
   runs would write the old version back over its work.
4. Run **Fence Lines**. It lists every saved map with a fence or guardrail line and
   how many sections each will get, asks once, and places them.
5. Open the map and click **Rebuild terrain**.

The line is now a chain of sections standing on the ground. A curve becomes short
straight sections, each one post spacing long (3 m, or 3.81 m for the steel W-beam),
tilted to the slope under its posts, the way a real fence crosses a bend. The run
stops on the last whole section, within half a section of where your line ends.

The line itself is hidden, not deleted, so you can change the fence later.

## Changing a fence afterwards

Move or reshape the hidden line, save, close the editor, and run Fence Lines again. It
replaces that fence; it never adds a second one.

## Steel guardrail ends

The steel W-beam gets **curled** ends. For the hazard or chevron plates instead, run
the app from a command prompt in its folder:

```
"Fence Lines.exe" --cap hazard
"Fence Lines.exe" --cap chevron
```

To convert one map only, add `--level` and the map's folder name, for example
`--level level_my_map`.

## How the sections join

Each style has two section models. The **link** (`_bay`) is a section without its far
post. The whole **section** (`_break`) has a post at both ends. A run is links, end to
end, closed by one whole section, so every joint has exactly one post and the run
ends on a post. Placing whole sections end to end would stand two posts on every
joint.

You can place either model by hand as well; both break.

## What is not known yet

- **Whether the hidden line still blocks trucks.** If it does, the sections in front
  of it would break and the truck would still stop. Until this is tested, if a run
  doesn't let trucks through, delete the line in the editor after converting it (you
  lose the easy re-run).
- **Which way the guardrail ends face at the start of a run.** They are worked out
  from the models and have not been looked at in the editor.
- The finished runs have not been driven into in a running game.
