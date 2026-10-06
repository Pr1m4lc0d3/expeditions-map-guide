---
title: The skills
part: AI tools
order: 820
summary: The written instruction sets that teach Claude Code or Codex how to work on this game, what each one covers, and how to install them.
---

# The skills

A skill is a folder containing a `SKILL.md` — a short document with a name, a
description of when it applies, and the instructions themselves. The agent reads
the description, decides the skill is relevant, and follows it.

They matter more than they look. Most of what is in them is not "how to use a
tool", it is **the rules that are invisible until you break them**: the editor
reads tiles and not masters, a CRLF subgroup file is silently ignored, an
absolute path makes the texture converter claim a file does not exist.

## Installing them

Copy the skill folder into your agent's skills directory. For Claude Code that
is `~/.claude/skills/<name>/SKILL.md`. The agent picks them up automatically and
you can also invoke one by name.

## What is here

### `expeditions-mapping`

Terrain, roads, rivers, models, zones and objectives. The whole map-making
surface. Its most valuable single instruction is to search the official
documentation **before** building anything, because the editor already has a tool
for most things people reimplement by hand.

Covers, among much else: that the editor builds from `data/<col>_<row>/` tiles
rather than the master images, that it reads those tiles when the map is
*opened*, that roads are overlay objects and not carved terrain, that heights are
R16F so there is a hard floor on smoothness, and that model scale is meaningless
without reading the mesh bounding box first.

### `expeditions-vehicle-port`

Bringing a SnowRunner vehicle into Expeditions, and specifically the black-truck
problem. Carries the texture encoder invocation, the ground-truth acceptance
test, the texture map conventions, and a list of the eighteen things that are
**not** the cause — which is most of its value, because each of them looks
plausible for hours.

See [Porting a SnowRunner truck](../65-vehicles/porting-a-truck.html).

### `expeditions-specialist`

Custom specialists: the persona definitions and the packing rules for them.

## Writing your own

The useful shape, learned from the ones above:

**Lead with the fact that changes behaviour.** Not background. The vehicle skill
opens with "meshes port, textures do not" because everything else follows from
it.

**Say what is *not* the cause.** A list of eliminated hypotheses is worth more
than a list of steps, because it stops the agent re-deriving a dead end you
already paid for.

**Record the error message, not just the fix.** `Unable to find texture file`
means "not underneath `-r`". An agent that knows that saves an hour.

**Mark what is measured and what is guessed.** Same discipline the rest of this
guide uses. An agent will treat a confident sentence as fact.

!!! note "Keep the description on one line and quote any colon"
    A skill description containing `: ` is read by strict YAML parsers as a
    nested mapping, and the whole file is rejected. Wrap it in double quotes.
