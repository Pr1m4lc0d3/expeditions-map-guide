---
title: Placing the engine ghost
part: Vehicles
order: 669
summary: The see-through engine the game shows at start-up sits at the truck's engine sound, not its steam or its engine damage box. Why it floats out of the nose on a new body, and the tool that puts it in the bay.
status: draft
---

# Placing the engine ghost

Start a truck in Expeditions and a see-through engine flashes up in its engine bay. It shows again
when the engine takes damage. On a truck you have built or brought in from somewhere else, that
ghost often appears in the wrong place: out past the grille, floating above the hood, or 20 cm off
to one side.

The fix is one line in the truck's class file. The hard part is knowing which line, because the two
obvious candidates do nothing.

## What the game reads

The ghost has three settings, and only two of them are named after it:

| Setting | Where | What it does |
|---|---|---|
| `EngineIconMesh` | `<TruckData>` | which ghost model to draw |
| `EngineIconScale` | `<TruckData>` | its size |
| `<Sounds Origin="(x; y; z)">` | the truck's `<Sounds>` element | **where it is drawn** |

The position comes from the **engine sound**. When the game loads a truck class it builds an
object for the engine sound from `<Sounds Origin>` (and `<Sounds ParentFrame>`, if the truck gives
one). The code that draws the ghost takes that object's place in the world, pulls it a little
toward the camera, and draws the ghost model there. Nothing else in the truck class sets it. The
game's own field list confirms this: the only fields with "EngineIcon" in their names are the mesh
and the scale.

This was read out of `Expeditions.exe` with IDA after two in-game attempts had failed. The parser
stores the ghost mesh and scale beside each other in the truck's data, and the only code that reads
them back is the drawer. The drawer positions the ghost from the engine-sound object, which the
parser fills from `<Sounds Origin>`.

!!! warning "Two settings that look right and do nothing"
    **`<Steam Origin>`** places the radiator steam, not the ghost. Moving it left the ghost exactly
    where it was. Stock trucks put their steam all over the place: one stock truck's sits 6 cm behind
    the truck's own origin, two metres from its engine.

    **The engine `<DamageArea>`** is the box that takes engine damage in a crash. On every stock
    truck it sits on the engine, which makes it look like the answer. It is not: moving it did not
    move the ghost either.

Coordinates are the truck's own space, in metres: **x forward, y up, z to the side**. `z` is not
always 0 on a ported truck: one ported Jeep carried a sound origin of `(0.81; 0.779; -0.2)`, which
is why its ghost sat 20 cm to one side.

## Why a new body gets it wrong

A truck built on another truck's class keeps that truck's `<Sounds Origin>`. If the old engine sat
further forward or higher than the new body's bay, the ghost follows the old engine. A truck
brought in from SnowRunner can also carry a sound origin that was never meant for the ghost at all.

## The ghost models

`EngineIconMesh` names a mesh in the game's `shared.pak`. Three are **generic**, modelled round
their own origin so they can go in any truck:

| Mesh | Size at scale 1 (length x height x width) | Reaches, from the origin |
|---|---|---|
| `env/engine_small` | 0.66 x 0.64 x 0.56 m | 0.28 back, 0.38 forward, 0.33 down, 0.31 up |
| `env/engine_default` | 1.12 x 0.66 x 0.67 m | 0.40 back, 0.72 forward, 0.43 down, 0.23 up |
| `env/engine_big` | 1.47 x 0.66 x 0.95 m | 0.48 back, 0.99 forward, 0.43 down, 0.23 up |

The origin is not the middle of the model. The default engine reaches almost twice as far forward
as back and sits mostly below its origin, so placing the origin "in the middle of the bay" puts the
engine too far forward.

The other ghost meshes are named after stock trucks (`env/engine_<truck>`). Those are modelled in
their own truck's space, already in place, so on another body they land wherever that truck's
engine was. Use a generic one on anything you build.

!!! note "A lift kit carries its own ghost"
    A suspension set can swap the whole truck for a **truck replacement**
    (`classes/truck_replacements/<name>.xml`). The replacement is a complete truck class with its
    own `EngineIconMesh`, `EngineIconScale` and `<Sounds>`. If your truck has one, place the ghost in
    both. That is also the only way a ghost can change with the build: the game reads the ghost from
    the truck (or its replacement), never from an engine add-on, so a V8 ghost can come with a lift
    kit but not with the V8 itself.

## Putting it in the bay

The **engine-ghost** tool in [expeditions-tools](https://github.com/Pr1m4lc0d3/expeditions-tools/tree/main/engine-ghost)
does the measuring. It reads the truck's own converted mesh out of the mod (no source files needed),
finds the engine bay, and fits the ghost in it:

```bash
python engine_ghost.py --mod "<...>/Mods/.modio/mods/<id>" --truck my_truck --preview bay.png
```

It reports where the ghost is now and what is wrong with it ("pokes 0.04 m out of the nose", "sits
-0.13 m off the centre line"), suggests a `<Sounds Origin>`, and draws a side and plan picture with
the bay, the hood line, the ghost now and the ghost suggested. `--apply` writes it into the mod's
pak (with the game closed), and `--raise`, `--lower` and `--forward` nudge it after you have looked.

How it finds the bay:

- **Nose**: the front-most bodywork that reaches near hood height. Bumpers, winches and bull bars
  sit lower and further out, and a winch bumper once put one truck's "front" 18 cm ahead of its grille.
- **Windshield base**: the front edge of the glass near the centre line, from just under the hood
  up. Headlight lenses are glass too, but they sit lower and further out.
- **Bay**: from 10 cm ahead of the windshield base to 15 cm behind the nose.

On the two trucks tested, the suggested front-to-back place landed within 2.5 cm of the place the
owner settled on by eye. **Height is a look, not a measurement.** On those same two trucks the
owner chose the ghost's top about 25 cm under the hood line on one and 8 cm under on the other, so
the tool's height is only a starting point: check it in game and nudge.

!!! tip "Converted meshes do not agree on where a part's vertices are"
    In some mod meshes a part's vertices are stored relative to its frame's whole parent chain (one
    truck's body sat a metre too low read raw). In others they are already in truck space (another
    truck's body landed 1.2 m outside its own mesh when the chain was applied). The tool takes,
    for each part, whichever reading keeps the most vertices inside the bounds in the mesh's own
    header, which is the box the game itself uses.

## What has been checked

- In game: `<Sounds Origin>` moves the ghost; `<Steam Origin>` and the engine `<DamageArea>` do not.
  Two trucks, one built from scratch and one ported, both placed and approved by eye.
- In the exe: the drawer reads the ghost's place from the engine-sound object, and no other field
  places it.
- Not yet checked: whether `<Sounds ParentFrame>` makes the ghost ride a tilting cab. The stock
  trucks that set it use the cab bone, so it should, but nobody has watched it happen.
