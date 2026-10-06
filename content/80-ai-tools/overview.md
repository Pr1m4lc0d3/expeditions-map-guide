---
title: Using AI with the editor
part: AI tools
order: 810
summary: What the AI augmentation layer is, what it is good at, what it must never be trusted with, and how it relates to doing the work by hand.
---

# Using AI with the editor

Everything in this guide can be done by hand. This section is about the other
way of working: driving an AI coding agent — Claude Code or Codex — that has been
given tools and written instructions for this editor specifically.

None of it is magic, and none of it replaces understanding the format. It is
closer to having a very fast assistant who has read all 514 pages of Saber's
documentation and will not get bored doing the same operation nine hundred times.

## What the layer is made of

There are three pieces and they stack:

**The toolkit** is a folder of plain Python scripts. They read and write map
files directly. They have nothing to do with AI — you can run them yourself from
a terminal, and the guide documents them that way. See
[the toolkit](toolkit.html).

**The skills** are written instructions that teach an agent how and when to use
those scripts, plus the hard-won rules about this engine that are not in any
official document. See [the skills](skills.html).

**The agent** reads the skill, picks the right tool, runs it, and reads the
result. Its value is that it already knows the traps.

## What it is genuinely good at

**Operations the hand tools structurally cannot do.** The editor's Flatten brush
levels ground to one horizontal height, so there is no hand tool that cuts a
bench holding a steady grade down a hillside. A script can.

**Scale.** Reseating two thousand models, checking every objective in a map,
converting a hundred textures, auditing a pak. Work where a human gets it right
the first fifty times and then makes one silent mistake.

**Reading the documentation.** Saber's guides are accurate and enormous. An agent
that searches them properly answers "how do I make a road" in seconds, which is
the single highest-value thing in this whole section. A full day was lost here
once, carving roads into a heightmap, while the editor's actual road tool sat
documented and unread.

**Remembering why.** Most rules in these tools exist because something failed
silently. The agent carries those with it.

## What it must not be trusted with

**Deciding what is true about your map.** An agent will happily tell you a
mechanism it inferred. Make it show you the measurement, or the page in the
official docs, or the line in the game data.

**Anything it has not verified.** The pattern that works is: run the tool, keep
the output, inspect the artifact the engine actually reads. "It converted without
error" is not the same as "it loads".

**Replacing the editor.** Terrain geometry, object placement, visual judgement
and the compile step are the editor's job. Scripts are for what it cannot do.

!!! warning "Three failed fixes means the approach is wrong"
    If an agent has tried three times and the thing is still broken, stop it. The
    useful move at that point is not a fourth attempt — it is questioning whether
    the diagnosis is right at all. The vehicle-porting work in this guide
    eliminated eighteen plausible causes before finding the real one, and every
    single one of those had looked convincing.

## The loop that actually works

When you build something by hand that you want turned into a tool:

1. Snapshot the files **before** you save.
2. Build one example of the feature. Save.
3. Diff, to recover the transfer function — footprint, magnitude, cut versus fill.
4. Turn that into a parameterised tool **and a test** that reproduces your
   original stroke within tolerance.

One stroke of the Smooth brush produced a complete filter specification this way.

**Never ship a generator with nothing to check it against.** The texture encoder
in the vehicle porting tool is trusted only because it reproduces, byte for byte,
a file the game itself produced.

## Where to start

<ul class="cards">
<li><a href="skills.html"><strong>The skills</strong><span>What each one covers and when it fires.</span></a></li>
<li><a href="toolkit.html"><strong>The toolkit</strong><span>The scripts, and how to run them yourself.</span></a></li>
<li><a href="../65-vehicles/porting-a-truck.html"><strong>Porting a truck</strong><span>A worked example of the whole loop, including the dead ends.</span></a></li>
</ul>
