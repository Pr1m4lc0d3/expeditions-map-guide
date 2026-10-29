---
title: How terrain actually works
part: The land
order: 210
summary: Heightmaps, the tile system, and why editing the file you think is the terrain often changes nothing.
---

Terrain in Expeditions is a grid of heights. The editor turns that grid into the
ground you drive on. That part is simple. What catches people out is *which* copy
of the grid the editor actually reads, *when* it reads it, and how precisely a
height can be stored at all.

This page covers those three things. Get them wrong and you can spend a day
editing a file the editor never looks at.

## Size and height are fixed when you create the map

A map is measured in **blocks**. Each block is 24 m square.
<span class="prov prov-doc">documented</span> You set the number of blocks and
the **Max height** when you create the terrain, and both are read-only in the
terrain properties afterwards.

| setting | value |
|---|---|
| block size | `24 m` |
| maximum blocks per axis | `84`, so a full-size map is `2016 m` square |
| minimum recommended | `5 x 5` blocks, because the edges carry an invisible wall |
| drone no-fly zone | `150 m` from the edge by default, so very small maps are a poor fit |

The level name must start with `level_`. <span class="prov prov-doc">documented</span>

Choose Max height with care, because you cannot change it later. A value of `512`
has been used on maps that load and drive in game.
<span class="prov prov-unver">measured</span> Whether values above `512` work has
not been tested.

## Where the heights live

A map keeps its height in more than one place. Only one of them is what the editor
builds from.

```
Media\prebuild\<map>.xml                  descriptor: blocks, Max height, materials
Media\prebuild\<map>\_height_source.png   a height image you can import (see below)
Media\prebuild\<map>\data\<col>_<row>\    16 TILES, each with its own _height.dds
Media\levels\<map>\height_map.dds         the BUILT result
```

Every map is split into **16 pieces**, `0_0` to `3_3`, whatever its size.
<span class="prov prov-doc">documented</span> Each piece has a folder under
`data\` holding that piece's height, masks and blends. The folder name is
**column first, then row**. <span class="prov prov-unver">measured</span>

!!! warning "The editor builds from the tiles, not from the big images"
    Editing a full-size master image, or `_height_source.png`, changes nothing
    in game on its own. The editor builds the terrain from the per-tile files in
    `data\<col>_<row>\`. The same is true of distribution masks: the editor reads
    the per-tile `dstr_*.tga`, not the master in `fullTexture\`.

    On one map, a road was graded in the master and the built terrain was then
    compared to both versions. It matched the old, ungraded master to `0.051 m`
    and the graded one to only `0.241 m`. The graded terrain sat on disk being
    ignored. <span class="prov prov-unver">measured</span>

!!! warning "Tiles are read when the map is opened"
    The editor reads the tiles **when you open the map**, not when you press
    Rebuild Terrain. If a script writes tiles while the map is open, the rebuild
    ignores them. Close the map, write, then reopen it.
    <span class="prov prov-unver">measured</span>

### Tile resolutions

Different layers are stored at different resolutions. Measured on a full-size
`84 x 84` map: <span class="prov prov-unver">measured</span>

| layer | pixels per tile |
|---|---|
| height, blends, distribution masks | `1008` |
| water foam and speed (`_water.tga`) | `651` |
| water mud (`_water_mud.tga`) | `63` |

The full-size master is four tiles plus one pixel: `1008 x 4 + 1 = 4033`. At
`2016 m` across that is `0.5 m` per height sample.

## Bringing in a heightmap from another tool

If you build terrain elsewhere, from real survey data or a terrain generator, you
import it with **Copy Source Heightmap**. Right-click the Geometry node in the
Scene View to find it. <span class="prov prov-doc">documented</span> It reads
`Media\prebuild\<map>\_height_source.png`.

Three things about that file are not what the name suggests:

- Saber describes it as a one-channel 16-bit image. On disk the editor's own copy
  is a **DDS file holding 16-bit floats**, despite the `.png` extension.
  <span class="prov prov-unver">measured</span>
- The editor creates it at **tile size**, a quarter of the master's width: `1008`
  pixels for a `4033` master, `48` for a `193` master.
  <span class="prov prov-unver">measured</span> Write it at the same size the
  editor made it.
- Copy Source Heightmap **replaces the whole terrain**. The file must carry every
  part of the map, including the parts you did not change.
  <span class="prov prov-unver">measured</span>

!!! warning "A baked terrain file beats everything"
    A map folder copied from another map carries that map's baked `data.stg`,
    `data_editor.stg` and `data_nx.stg`. The editor loads the old baked terrain
    and never looks at your new heights; the symptom is the previous map's ground
    with an empty Scene View. Move the three `.stg` files aside, reopen the map,
    and answer **Yes** when it offers to create the terrain file.
    <span class="prov prov-unver">measured</span>

## How precisely a height can be stored

This is the fact that most changes how you build roads.

Height tiles store each height as a **16-bit float**, a fraction of Max height.
<span class="prov prov-unver">measured</span> A 16-bit float has only about
three significant figures, and its precision is **relative**: the higher a point
is above zero, the coarser the smallest step it can take. The step doubles each
time the elevation doubles.

The steps for a map with Max height `512`, calculated from the format and
matching what was measured on real tiles:
<span class="prov prov-unver">measured</span>

| elevation | smallest possible height step |
|---|---|
| 16 to 32 m | `1.6 cm` |
| 32 to 64 m | `3.1 cm` |
| 64 to 128 m | `6.3 cm` |
| 128 to 256 m | `12.5 cm` |
| 256 to 512 m | `25 cm` |

On an upland road at about 200 m, the profile measured as a literal staircase:
median tread `1.5 m`, median riser `12.5 cm`, the exact step size. That is a
washboard. <span class="prov prov-unver">measured</span>

!!! note "Older figures"
    Earlier notes gave the step as a smooth `elevation / 2048`. That is the best
    case, not the rule. The real step jumps at each doubling of elevation and
    sits between `elevation / 2048` and `elevation / 1024`.

### What follows from that

**No filter can go below the step.** Smoothing, by hand or by script, lands at
one and a half to three times the step and no lower.
<span class="prov prov-unver">measured</span>

**Flattening a road makes the stepping more visible, not less.** The length of
each flat tread is the step divided by the grade. A gentler road has longer
flats and the same-height ledges between them. On rough ground the steps hide in
the noise; grade the road smooth and they are the only thing left. A grade above
roughly 4 degrees hides them. <span class="prov prov-unver">measured</span>

**Changing Max height does not help.** The step follows the real height of the
ground above zero. Rescaling cancels out.
<span class="prov prov-unver">measured</span>

**So route roads low.** Valley floors and creek bottoms have the finest
precision on the map. Below about 64 m the step is `3 cm` or less.

!!! tip "Measure grade over a sensible distance"
    A `0.2 m` step is a 40% grade over half a metre. Measure grade over about
    `15 m` of road, or you will chase slopes that no truck can feel.
    <span class="prov prov-unver">measured</span>

The built `levels\<map>\height_map.dds` is a 16-bit **integer** image at about
`0.39 cm` per step, 32 times finer. The engine can draw smooth ground; the source
format cannot feed it. <span class="prov prov-unver">measured</span>

## Writing heights back into the tiles

If a script edits heights in a master and then pushes them into the tiles, the
push must be a **merge**, never a straight copy.

The tiles hold hand sculpting done in the editor after the master was written.
On one map a rebuilt pond existed in one tile alone, and a road corridor ran
through it: almost every pixel near the pond was inside the area a road script
wanted to write, differing by up to `4.25 m`. A wholesale copy would have erased
it. <span class="prov prov-unver">measured</span>

A safe push:

- writes only pixels that the edit changed **and** that lie inside the area it
  meant to change
- protects water channels and their banks, plus a margin
- takes explicit no-go circles for ground you reshaped by hand
- caps how far it moves the ground. Keep it near `3 m`. Forcing a gradient onto a
  bad alignment once produced `30 m` embankments, and ground that differs from
  its surroundings by that much has a cliff at every edge.
  <span class="prov prov-unver">measured</span>

The toolkit's `push_heights.py` works this way for a road network: it writes
only inside the road corridor, protects water by default, and takes no-go
circles. It dry-runs by default and only writes with `--apply`. See [the
toolkit](../80-ai-tools/toolkit.html).

```
python push_heights.py level_<name> --protect-circle <x,z,radius>
python push_heights.py level_<name> --protect-circle <x,z,radius> --apply
```

!!! warning "Sometimes the tiles are the stale copy"
    The rule "the editor builds from the tiles" held for small edits to a built
    map. It did not hold everywhere. On one map, a whole column of four tiles
    disagreed with the master by `40 m` on average while the master was
    continuous across that boundary: the editor had rewritten the other tiles
    that morning and never touched those four. Pushing them back would have
    reverted the night's work. <span class="prov prov-unver">measured</span>

    Before treating either copy as the truth, compare the tiles against the
    built `height_map.dds`.

## Not yet known

- Why some tiles were left stale in the case above, and how to predict it.
- Whether a full-resolution `_height_source.png` (`4033` pixels instead of
  `1008`) imports correctly. One set of notes says it scales a quarter of the map
  over the whole; another says a full-size file loaded. This has not been
  settled by a clean test.
- Whether Max height above `512` is accepted.
- Whether neighbouring tiles share an edge pixel. Two measurements disagree.

## Before you build

Read Saber's own pages for the topic first. With the toolkit:

```
python wiki.py howto terrain
```
