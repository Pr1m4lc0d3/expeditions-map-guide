---
title: Rock lights on any truck
part: Vehicles
order: 667
summary: How a truck gets an add-on it was never built with, shown with rock lights, and the tool that adds a five-colour rock-light kit to your own truck or, on your own PC, to any truck.
---

# Rock lights on any truck

Rock lights are small LED pods under a truck, one in each wheel well and a few along the
frame, that light the ground around it at night. No truck in the game has them. This page
explains how they are added, because the same method gives any truck any add-on it was not
built with.

There are two ways to get them:

| You want | Use |
|---|---|
| Rock lights on the trucks that came with the game | The **Doc's Rocks Rock Lights** mod on [mod.io](https://mod.io/g/expeditions/m/rock-lights). PC only, one installer |
| Rock lights on a truck you are building, or on a truck mod you have installed | The [rock-lights tool](https://github.com/Pr1m4lc0d3/expeditions-tools/tree/main/rock-lights) in expeditions-tools |

## How a truck takes an add-on

A truck only offers the add-ons it has a **slot** for. The slot is an `AddonSockets` entry in
the truck's class file, and every add-on names the slot it fits with `InstallSocket`:

```xml
<!-- in the truck's class, inside <GameData> -->
<AddonSockets>
    <Socket Names="RockLightsMyTruck" ParentFrame="BoneChassis_cdt" />
</AddonSockets>

<!-- in each add-on's class -->
<InstallSocket Type="RockLightsMyTruck" />
```

So adding a new kind of add-on to a truck is two jobs: give the truck an empty slot, and make
add-ons that fit it. The slot changes nothing until the player fits something in it.

Where the truck's class lives decides how hard the first job is:

- **Your own truck.** The class is in your Media folder. You edit it, and the editor packs it
  with your mod.
- **Someone else's truck mod.** The class is inside that mod's pak. On your own PC you can
  change it; the tool below does it and keeps a backup.
- **A truck that came with the game.** The class is in the game's own `initial.pak`, and a mod
  cannot add a slot to it. That is why the Rock Lights mod is a manual install with a patcher:
  the patcher adds the slots to `initial.pak`, and the kits ride in an ordinary mod. Consoles do
  not allow changing game files, so this route is PC only.

## What a rock-light kit is

Each kit is one add-on class with three parts.

**The lights.** Eight spot lights in the add-on's `<ModelAttachments>`, in the `Ignition`
group, so they are on whenever the engine runs. A truck light has no day and night setting,
so there is no better group for them. Each light is a `Light` aimed at the ground, with a
`Flare` for the glow on the lens:

```xml
<ModelAttachments>
    <Ignition>
        <Light _template="IgnitionSignalWhite" Color="g(255; 160; 30) x 26.4"
               Pos="(0.70; 0.96; 0.69)" Dir="(0.30; -0.68; 0.68)"
               AttenEnd="7.0" InnerCone="60" OuterCone="150" ParentFrame="BoneChassis_cdt" />
        <Flare _template="IgnitionSignalWhite" Color="g(255; 160; 30) x 0.9" Size="0.05" ... />
    </Ignition>
</ModelAttachments>
```

Stock truck lights run at a multiplier of 1 to 2; the main headlight runs at 6.5. Rock lights
need far more, around 25 to 30, because their light lands on the ground a hand's width away
and still has to read from the driver's seat.

**The pods.** A small mesh: a 2 in pod for every light, each on a bracket that runs to the
truck's own frame or floor, with a bolted tab.

**The model line.** This is the part that goes wrong:

```xml
<PhysicsModel Mesh="trucks/rock_lights_pods_my_truck" />
```

!!! warning "No `<Body>` on a small add-on like this"
    Many add-ons carry a `<Body>` under `PhysicsModel`. On these kits it made the garage fit
    fail without any message: the kit was listed, it highlighted, and **Buy** did nothing.
    The test is simple. **Highlight an add-on in the garage before buying it. If it does not
    show on the truck, the model setup is wrong**, whatever the class file looks like.

## Where the pods go

Every truck is a different size, so the tool places the pods from the truck itself, not from
fixed numbers:

1. **From the wheels.** The class's `<Wheel Pos>` values give the front and rear axles and the
   track width. One pod goes behind each front wheel, one ahead of each rear wheel, and two
   under the frame on each side, all at the same proportions on every truck.
2. **From the frame height.** Trucks that carry a `BoneChassis_cdt` frame start the pods at
   its height. On trucks without one, the tool measures the underside directly.
3. **Onto the steel.** For each pod it reads the truck's own converted mesh and looks straight
   up and straight inward for metal within a short bracket's reach. If there is none, the pod
   moves a little lower or further in until there is. The light moves with the pod.

Placing pods from proportions alone is not enough. On tall trucks the frame sits well above
the wheel centres, and pods placed that way floated beside the rails with brackets reaching
into nothing.

## Adding rock lights with the tool

The tool runs on its own, with no AI and no internet. You need Python, Blender and the
Expeditions editor; the [README](https://github.com/Pr1m4lc0d3/expeditions-tools/tree/main/rock-lights)
lists the details. Close the game first.

Run it with no arguments and it asks you, step by step: your own truck or an installed mod,
which truck, then it shows where each pod goes and asks before it changes anything.

- **No Python?** Download **Rock Lights Tool.exe** from the repository's
  [Releases](https://github.com/Pr1m4lc0d3/expeditions-tools/releases) and double-click it.
  It still needs Blender and the editor.
- **Using an AI assistant?** Point it at the tool's
  [AGENTS.md](https://github.com/Pr1m4lc0d3/expeditions-tools/blob/main/rock-lights/AGENTS.md)
  and ask it to add rock lights to your truck. That file gives it the whole job.

```
python add_rock_lights.py
```

Or say it all at once:

```
python add_rock_lights.py --truck my_truck                          # your truck, in Media
python add_rock_lights.py --truck their_truck --mod-dir "<mod folder>"   # an installed mod
python add_rock_lights.py --truck my_truck --plan                   # show placement only
python add_rock_lights.py --truck my_truck --remove                 # take it out again
```

Either way the truck gets five kits, **Rock Lights - White, Amber, Red, Blue and Green**, in
its **Miscellaneous** garage tab.

- **Your own truck:** the kits, the pod mesh and its texture go into your Media folder, and the
  slot into your truck's class. Pack your mod as you always do.
- **An installed mod:** the tool edits that mod's paks, after one backup of each
  (`*.rocklights_bak`). An update of that mod from mod.io replaces its paks, so run the tool
  again afterwards. `--remove` takes out exactly what it added.

The kits must live in the same mod as the truck. A mod's classes are filed under that mod's
id, so a slot and a kit in two different mods never meet.

## Sharing what you made

Changing a truck on your own PC is yours to do, whoever made it. **Uploading** someone else's
truck with your rock lights on it is not, unless its author says you may or its licence
allows it. If the truck is yours, ship the kit with it like any other add-on.

## What has been checked

- The kits, the brightness, the placement method and the pods have been checked in game on the
  trucks that came with the game.
- The tool reproduces that placement on every one of those trucks to the millimetre.
- On truck mods, the tool's output has been checked file by file: the five kits, the slot, the
  pods and the texture, and a removal that gives back the original paks byte for byte.
- On a truck mod in game: a tube-frame buggy from mod.io got its kits from the tool, the pods
  showed in the garage, and the lights came on.
- The tool never touches the game's own `initial.pak`. Only the trucks that came with the game
  need that, and the Rock Lights mod's patcher does it for them.
