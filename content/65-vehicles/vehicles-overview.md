---
title: Vehicles, and what this part covers
part: Vehicles
order: 640
summary: A map of the chapter. Bringing a truck in from SnowRunner, the things that break silently when you do, and where each one is written down.
---

# Vehicles

Expeditions and SnowRunner are both Saber engine games sharing one mod format,
which is why a SnowRunner vehicle can be brought across at all. Its meshes load
untouched.

Everything else is where the work is, and the governing fact of this whole
chapter is worth stating once:

!!! danger "Nothing in a vehicle port reports an error"
    Not a texture the game cannot decode, not a missing addon class, not a dead
    tyre set, not an undeclared image field, not a flipped texture. The game
    logs almost nothing and falls back to nothing. **The truck spawns, drives
    and looks nearly right while being wrong.**

    So an unverified step is not a step you got away with. It is a defect you
    have not found yet — and quite possibly one someone else will find in your
    released mod.

## Where to start

| if you are | read |
|---|---|
| doing a port, right now | **[Porting runbook, start to finish](porting-runbook.html)** |
| wondering why your truck is **solid black** | [Porting a SnowRunner truck](porting-a-truck.html) |
| missing bumpers, a spare wheel, or tyre options | [Accessories and tyres](addons-and-wheels.html) |
| fixing store and garage pictures | [Store and garage artwork](store-and-garage-images.html) |
| adding paint schemes, chrome or camouflage | [Skins and paint](skins-and-paint.html) |
| stuck, with no error to go on | [Diagnosing a vehicle](diagnosing.html) |

The runbook is the ordered procedure and every other page in this part is a
deeper read on one of its steps. If you only read one thing, read that.

## The shape of the problem

Three different kinds of failure turn up in a port, and telling them apart saves
a lot of time:

**The target game cannot read what the mod ships.** Textures encoded by the
other game's converter. One cause, one fix, and it accounts for the single most
dramatic symptom — a completely black vehicle.

**The mod depends on something only the donor game has.** Addon classes for its
bumpers, wheel classes for its tyres. The mod is not broken; it is simply
incomplete outside the game it was built in. You either bring the dependency
across or substitute a local equivalent.

**The mod never declared something the UI needs.** Image fields, mostly. These
are the quietest of the three because the file is often right there in the pak
with nothing pointing at it.

A tool can find all three and is in the
[toolkit reference](../80-ai-tools/toolkit.html). The same tooling is published
on its own as the
[Expeditions Vehicle Importer](https://github.com/Pr1m4lc0d3/expeditions-vehicle-importer)
if you want it without the rest of this guide.

## What this part does not cover

**Making a vehicle from scratch.** Modelling, rigging and exporting a new truck
is a different discipline, and this chapter assumes you are bringing across
something that already exists.

**Permission.** Porting someone else's mod to another game is their call. Ask
first, and credit them. Nothing here redistributes anyone's work and neither
should you.
