---
title: Making your own overlays
part: The land
order: 235
status: draft
summary: The files behind a road, fence or guardrail you draw like a road, how to write your own, and how to give it a picture in the editor's library.
---

Every road, track, fence line and guardrail line in the editor's overlay list is an
**overlay type**: a small class file that says how to draw it, plus its textures, and for
a fence, a mesh. The game's own types live inside its paks. Yours go in your own `Media`
folder, `Documents\My Games\Expeditions\Media`, and the editor lists them next to the
game's. [Roads are not carved terrain](roads.html) covers laying one; this page covers
making one.

There are two kinds:

| Kind | What it is | Example |
|---|---|---|
| **Painted** | A texture laid over the ground along your line, which can also reshape the ground under it | Roads, trails, tracks |
| **Geometric** | A short mesh repeated along your line and pressed onto the ground | Fences, guardrails, walls, pipes |

!!! note "How much of this is tested"
    Fourteen painted roads built this way have been laid and seen **in a running game**
    on a locally installed map. Geometric fence and guardrail lines built this way convert
    and draw in the editor. The library pictures were seen in the editor after the fix
    below. A map installed from mod.io has not been tested.
    <span class="prov prov-unver">measured</span>

## Names and where the files go

Pick a name of lowercase letters, digits and underscores that the game does not already
use, such as `my_gravel_road`. Every file carries it:

```
Media\classes\overlays\my_gravel_road.xml                the class
Media\textures\overlays\my_gravel_road__d_a.tga          colour (painted)
Media\textures\overlays\my_gravel_road_relief__d_a.tga   relief and coverage (painted)
Media\prebuild\common\my_gravel_road__s.tga              ground shape, optional (painted)
Media\meshes\overlays\my_fence_line.fbx                  the mesh (geometric)
Media\meshes\overlays\my_fence_line.xml                  its materials (geometric)
Media\icons\overlays_my_gravel_road.dds                  the library picture
```

Save every class and mesh `.xml` with bare `LF` line endings. Restart the editor after
adding a type; it lists the name with `\Media` after it.

## A painted road

### The class

This is a working two-lane highway's class, as shipped:
<span class="prov prov-unver">measured</span>

```xml
<OverlayBrand
	IsClampV="true"
	HeightMapBlendingContrast="0.9"
	BlendBorderMin="0.0"
	BlendBorderMax="0.4"
	IsAsphalt="true"
	IsExtrudable="false"
	GenerateDust="false"
	WheelTracks="0"
	Texture="overlays/my_highway__d_a.tga"
	TextureRelief="overlays/my_highway_relief__d_a.tga"
>
	<Prebuild
		DefaultWidth="16"
		FlattenPart="1"
		LandmarkColor="(110; 110; 110)"
		LandmarkPart="1"
		Layer="5"
		HeightmapOffset="my_highway__s.tga"
	/>
</OverlayBrand>
```

The paths in `Texture` and `TextureRelief` are relative to `Media\textures`; the one in
`HeightmapOffset` is a file in `Media\prebuild\common`. `DefaultWidth` is the width in
metres the road is drawn at. The rest were copied from the game's own road classes:
`IsAsphalt`, `GenerateDust` and `IsExtrudable` (a road that can sink into mud) set what
the surface is like, `LandmarkColor` is its colour on the navigation map, and `Layer`
decides which road draws on top where two cross. What each value does in detail has not
been measured. <span class="prov prov-unver">unverified</span>

To paint with **one of the game's own road textures**, point `Texture` at it, for example
`overlays/dirt_road_pbr__d_a.tga`, and ship only your relief and shape. The game supplies
the colour.

### The textures

Measured on the game's own roads: <span class="prov prov-unver">measured</span>

- **Colour** (`__d_a`) and **relief** (`_relief__d_a`): `2048 x 1024` TGA. The long side
  (columns) runs **along** the road and repeats; the short side (rows) runs **across** it,
  from one edge to the other.
- The **alpha of the relief** is the coverage: `255` draws the road, `0` shows the map's
  own ground. Fade it at the edges, or leave a grass strip down the middle of a two-track.
- **Ground shape** (`__s`, optional): `256 x 128`, 24-bit TGA, rows across the road again.
  Grey `128` leaves the ground alone; each grey level up or down moves it about `1.5 cm`,
  in a straight line (grey `12` dug `1.65 m`, grey `192` raised `0.96 m`, on a map with
  MaxHeight `64`). A crown is lighter in the middle; ruts are two darker bands. It is
  applied on top of Flatten only when the overlay's **Apply Offset** is on.

The editor converts the textures the first time it loads a map that needs them. It may
stop responding for a minute while it does; leave it.

## A geometric overlay

### The mesh

Model **one section**, such as one fence bay, running along Blender's **+Y** from its start,
centred on `x = 0`. The editor repeats it along your line and bends it to the ground. Saber's
guidance asks for a section symmetrical about X. <span class="prov prov-doc">documented</span>
Let nothing pass the section's two ends: a post that sits wholly past an end shows up twice
at every join, so put half a post at each end and the two halves meet.
<span class="prov prov-unver">measured</span>

Export it as `Media\meshes\overlays\<name>.fbx` and write its material file beside it:

```xml
<CombineXMesh Type="Overlay">
	<Material Name="fence" AlbedoMap="overlays/my_fence_line__d.tga"
	          NormalMap="overlays/my_fence_line__n_d.tga"
	          ShadingMap="overlays/my_fence_line__sh_d.tga" />
</CombineXMesh>
```

**`Name` must be the material's own name inside the FBX.** A name that matches nothing drew
the whole fence plain white. For wire or mesh with see-through parts, use a `__d_a` texture
and add `AlphaKill="true" TwoSided="true"`. <span class="prov prov-unver">measured</span>

### The class

```xml
<OverlayBrand NoVeryFar="true" WithTailOffset="false">
	<Prebuild OverlayType="GeometricConform" />
</OverlayBrand>
```

`GeometricConform` makes it a mesh pressed onto the ground. Leave out
`WithTailOffset="false"` and both ends of every run sink into the ground, so the top rail
slopes down and two runs cannot be joined. The game's own `racetrack_fence_us07` sets it
the same way. <span class="prov prov-unver">measured</span>

A geometric overlay stops a truck but **never breaks**: it is one mesh with no parts.
[Breakable fences and guardrails from a line](../30-dressing/fence-lines.html) explains why
and how to swap a line for sections that do.

## A picture in the editor's library

Without a picture, the editor draws its own: a painted road shows its texture, and a
geometric overlay shows an empty grey square. You can give it a picture, but the editor
needs a fix first.

### Why your picture never shows

The library looks for `Media\icons\<kind>_<name>.dds`. For a custom piece the name it uses
ends in `\Media`, so it asks for `icons/overlays_my_road\Media.dds`. The editor's file
system only splits paths on `/`, so that file is never found, wherever you put it. This
was traced in the running editor: the same check finds `icons/overlays_my_road.dds` and
`icons/overlays_my_road/Media.dds`, but never the path with `\`.
<span class="prov prov-unver">measured</span>

**Editor Pictures Fix** changes 41 bytes of `ExpeditionsEditor.exe` so a path ending in
`\Media.dds` is looked up as `.dds`, which loads your picture. The game's own pieces are
untouched. It keeps a backup beside the exe and can put it back. A game update replaces the
editor, so run it again after one. Run it with the editor closed:

```
python editor_pictures_fix.py            apply (asks first)
python editor_pictures_fix.py --check    only say whether it is applied
python editor_pictures_fix.py --undo     put the backup back
```

It is in [overlay-tools](https://github.com/Pr1m4lc0d3/expeditions-tools/tree/main/overlay-tools),
and the road, fence and guardrail packages on the [Downloads](../00-start/downloads.html)
page each install it as an app.

### The picture file

`128 x 128`, uncompressed 32-bit `A8R8G8B8` DDS, with a see-through background, the same
as the game's own pictures. **The library ignores the alpha and shows the colour under it.**
The game's pictures are light grey `(200, 200, 200)` where they are see-through; a picture
with black there shows as a black square. <span class="prov prov-unver">measured</span>

`make_icon.py` (same folder) writes one from any image, over the right grey:

```
python make_icon.py overlays my_gravel_road my_gravel_road__d_a.tga --square
python make_icon.py overlays my_fence_line my_fence_render.png
```

For a road, `--square` takes the middle of its own colour texture, as the game's roads do.
For a fence, render one section at three-quarter view on a transparent background.

The editor reads library pictures **the first time a list is opened** in a session. To see a
new picture, restart the editor.

## After every Pack terrain

A packed map draws a custom road as bare, levelled ground with no surface, for the same
reason a custom model drops a packed map to the main menu: the game registers it under one
name and looks it up under another. Run the after-pack fix after **every** pack, as
described in [Making your own models](../30-dressing/making-models.html#after-every-pack-terrain).

## Not yet known

- What each class value (`Layer`, `IsExtrudable`, `HeightMapBlendingContrast`,
  `BlendBorderMin` and `Max`) does in detail.
- Whether the ground-shape scale is fixed or follows the map's MaxHeight.
- Whether custom overlays on a map installed from mod.io draw on other players' machines.
