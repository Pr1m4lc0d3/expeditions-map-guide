---
title: The brushes
part: The land
order: 220
summary: Size, falloff and strength, and why a soft brush where a hard one belongs turns a road into a row of domes.
---

A brush is how you change the ground by hand in the editor. You pick one in the
Scene View, set three numbers, and paint. Almost every brush in the editor works
the same way, so learning one teaches you most of them.

## How painting works

Select a brush by selecting its node in the Scene View. The Geometry node and its
sub-nodes are the terrain brushes. <span class="prov prov-doc">documented</span>

- **Hold the right mouse button** and move to paint.
- **Click the left mouse button** to apply what you painted.
- **Undo Current Changes** in the brush dialog throws away everything since your
  last right-click.
- Then **rebuild** to see the result: right-click the scene and choose Rebuild
  Terrain, or Rebuild visible / Selection for part of it. The toolbar's
  **Enable autorebuild terrain** rebuilds each time you switch brushes.

<span class="prov prov-doc">documented</span>

## The three controls

Every brush has the same three controls. <span class="prov prov-doc">documented</span>

| control | what it does |
|---|---|
| **Size** | the brush's size, in metres |
| **Value** | how hard each pass pushes, and in which direction. Negative values are allowed: on the height brush, positive raises and negative digs |
| **Falloff** | how soft the brush's edge is. `0` is a completely hard edge. `1` starts fading straight from the centre |

Two more appear on many brushes:

- **Autofade** weakens the stroke depending on the direction you draw. Saber
  suggests it for ruts and mud.
- **Randomize** varies the strength randomly within a range, for rough,
  chaotic ground.

!!! warning "Some brushes do nothing at their default value"
    On brushes whose Value runs from `0` to `1`, a value above `0.50` paints and
    a value below `0.50` removes. The default is usually `0.50`, which does
    nothing until you move it. <span class="prov prov-doc">documented</span>

### Falloff is the control that matters most

**Falloff 0 is a hard brush.** It changes the whole circle by the same amount,
so it leaves a flat top with steep sides. That is what you want for a bench, a
wall, a step or a road bed.

**Falloff 1 is a soft brush.** The effect fades from the centre outwards, so each
dab leaves a rounded dome. That makes bumps and mounds.

!!! danger "A soft brush on a road makes a row of domes"
    Dragging a soft brush along a road leaves one rounded dab after another, and
    the road comes out as a line of humps rather than a bench. If you are
    building something with a flat top, use a hard brush.

    On the same stretch of road, a hard brush removed 42% of the roughness and a
    soft one 32%. <span class="prov prov-unver">measured</span>

**Size** has its own trap: too big, and it erases the shape of the land along
with the defect you were aiming at. **Value times the number of passes** is how
thorough the job is. More gentle passes give you more control than one strong
one.

## The main Geometry brush

Select the Geometry node itself and the brush has three modes.
<span class="prov prov-doc">documented</span>

| mode | what it does |
|---|---|
| **Height** | raises the ground, or lowers it with a negative Value |
| **Flatten** | levels the area to the height **under the centre of the brush** when you click |
| **Smooth** | evens out height differences. Saber recommends Falloff close to `0` |

### What Smooth actually does

Smooth sounds like a blur. It is not. One hand stroke of the Smooth brush along
`203 m` of road was saved and compared with a copy taken seconds before:
<span class="prov prov-unver">measured</span>

- **It only cut.** `9,174` pixels were lowered and **none** were raised. That
  is not a one-sided filter. On a road that slopes across, the
  average height inside a round brush sits below the crown, so the brush pulls
  the road down into the hill. On a sidehill, that benches the road, which is
  what a real road is.
- **It removes a narrow band of bumps.** The strongest effect was on bumps
  `2.4` to `2.9 m` long. Anything longer than about `5 m` came through intact.
  So it takes the washboard off a road and leaves the road's shape alone.
- **The brush was small**, a radius of about `1` to `1.5 m`.
- Roughness fell from `27.3 cm` to `17.6 cm`, and the worst step from `62.5 cm`
  to `37.5 cm`.

!!! note "Smooth cannot fix a hump"
    Because Smooth leaves anything longer than about `5 m` alone, it will not
    touch a hump that is tens of metres long. That needs a deliberate cut. See
    [roads](roads.html).

Smooth also cannot take the ground below the smallest step the height format can
store. See [how terrain works](terrain.html).

## Sculpting is iterative

Real terrain work is a sequence: raise a shoulder, flatten its top, smooth where
it meets the hill, then lower part of it because the first pass overshot.

**Measure between strokes.** In one recorded sequence, the third stroke made the
road rougher (`5.7` to `6.3 cm`), and only measuring caught it.
<span class="prov prov-unver">measured</span>

## When a script is genuinely the only option

Use the editor's brushes. Do not rewrite them in a script. Script only what the
hand tools structurally cannot do.

The clearest case: **Flatten levels to one horizontal height.** A road down a
hillside needs a bench that *descends* at a steady grade, and there is no hand
brush for that. You can only approximate it with many short flat steps.

Other cases where a script earns its place:

- switchbacks laid at a constant gradient
- anything whose target height changes continuously along a path
- the same operation over a whole road network

The toolkit's `sculpt_roads.py` runs the three-stroke sequence measured from hand
work over a whole network: flatten to a target that descends along the road,
then a small hard cut-only smooth, then a wider soft smooth to blend the
shoulder into the hill. On one road it took roughness from `26.0` to `9.5 cm`
with about `1.7 m` of cut, measured in the map files. Nobody has yet driven the
result in game. <span class="prov prov-unver">not checked in game</span> It
protects water, takes no-go circles for hand-sculpted ground, and limits how far
it moves the ground (`--max-move`, default `3 m`).

```
python sculpt_roads.py level_<name>
python sculpt_roads.py level_<name> --protect-circle <x,z,radius> --apply
```

Like every toolkit script it dry-runs unless you pass `--apply`. Close the map in
the editor before writing, because the editor reads the terrain tiles when the
map opens. See [the toolkit](../80-ai-tools/toolkit.html).

!!! tip "Turn a hand stroke into a tool"
    The most reliable way to script a brush is to copy one. Snapshot the tiles,
    make one stroke by hand, save, and compare the two. That gives you the
    footprint, the strength and whether it cut or filled. Build the tool from
    that, and keep the hand stroke as its test: the tool must reproduce it.

## The other Geometry brushes

The sub-nodes under Geometry work the same way and paint other layers.
<span class="prov prov-doc">documented</span> A few are easy to confuse:

- **Water** does not create water. It paints foam, speed and flow on water you
  have already added. See [rivers and lakes](water.html).
- **WaterMud** only changes the colour of a river, blending its clean and muddy
  colours. It does not make ground muddy.
- **Mud** and **Wetness** are separate brushes. Saber says the wetter a surface,
  the more a vehicle gets stuck, even where no mud is painted.

Saber's pages cover each one. With the toolkit:

```
python wiki.py howto terrain
```
