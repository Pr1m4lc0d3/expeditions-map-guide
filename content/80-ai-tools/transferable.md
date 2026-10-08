---
title: Lessons that transfer to other games
part: AI tools
order: 840
summary: None of this game's file formats carry over to another game's editor. The working method does, and so do the specific ways an AI agent fails silently against a closed toolchain.
---

# Lessons that transfer to other games

Nothing in the formats carries over. A different game has different containers,
a different scene graph, a different height encoding, and its own undocumented
rules. Reading this guide teaches you nothing reusable about *Farming Simulator*
or *Cities: Skylines*.

The method carries over completely. So does the failure catalog, because the
failures are not caused by this game. They are caused by an agent that writes
confidently into a format it cannot execute, against an editor that reports
nothing when it disagrees.

Every number below was measured on this project.

## The docs almost certainly already answer it

A full day went into carving roads into a heightmap. The editor has a road tool.
It is called Overlay, it was in the official documentation the whole time, and
the query was never made. A second day went to reimplementing a smoothing
filter that the Geometry Smooth brush already was.

So the first move on any new game is to get its documentation into a form the
agent can query, and the second is to query it before building.

**Then test the search with a question, not a keyword.** Searching "overlay"
finds the overlay page. That is useless, because you only search "overlay" once
you already know the answer. Asking "how do I make a road" returned nothing for
months. A search tool validated on terms you already know will pass every test
and fail every real use.

## The editor is the tool; scripts are for what it cannot do

The hand tools win by default. They are the thing the format was designed
around, and anything they produce is correct by construction.

Script only the operations the hand tools structurally cannot perform. In this
game that list is short and specific: a bench that holds a constant grade while
descending a hillside, because the Flatten tool levels to one horizontal height
and there is no graded-bench tool at all. Everything whose target varies
continuously along a path. Bulk work across a whole network.

That test transfers. Ask what the hand tool cannot express, not what would be
faster to script.

## Find the write path before writing anything

A mud-painting tool was written, tested, and reported success. The editor
produced no mud, because the two files it wrote, `extrude_map.dds` and
`_merge_mud_wetness.tga`, are **build outputs**. The editor overwrites them. The
writable layer was somewhere else entirely.

Worse, the same class of error produced a confident lie. A water-seating tool
reported "84.8% to 0.00% floating" while writing files the editor could not
read. It had measured its own intent.

Two rules come out of that, and both transfer:

- **A toolchain has inputs, working state, and outputs. Identify which is which
  before you write.** Here the editor compiles from per-tile files under
  `data/<col>_<row>/`, never from the full-resolution masters, and it reads them
  **when the map is opened**, not when you press Rebuild Terrain. An agent that
  writes tiles while the map is open watches its work get discarded.
- **Measure the artifact, not the operation.** "I wrote the file" is not "the
  game changed".

## A zero-result is a claim

This is the highest-value habit on the list, and it is free.

A search for a string returned no matches in three files that contained it,
because the search tool skipped hidden directories by default. A whole
ruled-out table got built on that absence.

**Run a positive control before citing a zero.** Search for something you know
is there, in the same place, with the same tool. If the control fails, the zero
means nothing.

## The peak: a constant that was right on one map in twelve

Three tools that move and re-seat 3D objects each carried this line:

```python
MAX_HEIGHT = 256.0
```

Heights are stored normalised from 0 to 1 and multiplied by the map's own
maximum elevation. Across the twelve maps on disk that value is 512 on five of
them, 256 on exactly one, and 244, 200, 184 or 64 on the rest. So the ground was
being evaluated at half its true elevation on the large maps and at four times
on the small ones.

Here is what makes it the lesson rather than a bug report. Asked to find objects
floating above the ground or buried in it, the tool reported:

```
0 buried, 0 floating, worst 0.00 m   -- across 16,589 models
```

A clean bill of health. After reading the elevation from the map descriptor
instead of assuming it, the same command on the same unchanged files reported
**6,637 buried over 0.30 m and 2,425 floating over 0.10 m, worst 2.12 m.**

The bug had been silently corrupting object placement across eleven of twelve
maps for as long as the tools existed, and it had been reporting zero defects
the whole time. Nothing crashed. Nothing warned.

**So: no magic numbers, ever. Read every geometric constant out of the project
file.** An agent will happily hard-code the first value it sees working, and that
value will be correct on the map in front of it.

## Your libraries will quietly rewrite your data

Python's `zipfile` normalises backslashes to forward slashes **when it reads an
archive**. On an untouched shipped map file, 19 of 31 member names come back
different from the bytes on disk. Rebuild that archive by copying the names
through and the game stops finding those members, and the map disappears from
the level list with no error, no log line and no crash dump.

The fix was to stop asking the library and parse the container directly. It then
turned out the real naming convention is mixed on purpose: all-backslash under
one prefix, all-forward under another, first-forward-then-backslash everywhere
else. A rule derived from the raw bytes reproduced 49 of 49 names across four
shipped files. Any attempt to tidy it would have broken the map.

**When you are matching a closed format, read the bytes, and copy the working
spelling instead of normalising it.**

## "Repeat until clean" is an assumption, not a method

A road grader was asked to iterate until the surface was smooth. Measured by
count of remaining defects, per pass:

| pass | humps | RMS |
|---|---|---|
| 1 | 9 | 0.116 |
| 2 | 18 | 0.126 |
| 3 | 27 | 0.136 |
| 4 | 31 | 0.149 |

Each pass re-derived its target from terrain the previous pass had moved, so it
chased its own output. The process diverges, and one pass is the best it gets.

Two things transfer. **Write the measurement before the fix**, so "better" is a
number rather than an impression. And know the floor: heights here are 16-bit
floats over the map's elevation, which puts the smallest representable step at
25 cm on a 512 m map, so a perfectly graded road still measures about 0.12 m of
roughness. Four of those passes were spent chasing quantisation.

## One backup is correct for one change and wrong for a loop

The grader wrote one backup per file under a fixed name, overwritten each run.
That is the right pattern for a single edit, and it is why four passes left no
way back: the original heightmap was overwritten four times and is gone.

**Take one immutable snapshot before a loop starts, outside whatever backup slot
the tool manages.** Related, from the same week: this editor has no autosave, and
a crash cost two hours of hand placement that no script could reconstruct.

## Make the human's example into the test

The pattern that produced the most reliable tools here:

1. Snapshot the files before the person touches anything.
2. They build one example by hand, in the editor, and save.
3. Diff for the transfer function: footprint, magnitude, whether it cuts or
   fills, what it leaves alone.
4. Write the tool, and write an acceptance test that reproduces their example
   within a tolerance.

One stroke of a smoothing brush yielded a complete filter specification that
way, down to which wavelengths it attenuated and the fact that it only ever cut.

**Never ship a generator with no reference to check it against.** The reference
is what separates a tool from a confident guess, and a closed toolchain will not
supply one.

## The shortest version

| | |
|---|---|
| Before building | query the docs; test your search with a question |
| Before scripting | name what the hand tool structurally cannot do |
| Before writing | identify input vs working state vs build output |
| Before claiming | run a positive control on every zero |
| Before trusting a constant | read it from the project file |
| Before trusting a library | read the bytes |
| Before iterating | write the measurement, and find the floor |
| Before a loop | take one immutable snapshot |
| Before shipping a tool | build the acceptance test from a hand-made example |

The common thread is that a closed toolchain fails silently. It does not raise,
it does not log, and it does not refuse. It accepts the write, discards it, and
loads the old map, which is why every item above is a way of getting a number
out of the artifact instead of out of the agent.
