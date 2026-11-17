---
title: Custom licence plates
part: Vehicles
order: 668
summary: How a truck can wear your own licence plate. The plate is an add-on that covers the plate the truck already carries, and one converted mesh can show any number of different plates.
status: draft
---

# Custom licence plates

A truck in the game carries a licence plate only if its maker modelled one. This page explains
how your own plate can replace it, and which trucks that works on. The **Doc's Rocks Plate
Maker** (PC only, on mod.io) does all of this from a small Windows program.

The rule it follows: **a truck that comes with no plate gets none.** The custom plate only
replaces a plate that is already there.

## Where the plates are

**Trucks that came with the game.** The plate is a real piece of the **front bumper** mesh, not a
picture painted on the body. Most share two plate textures (`license_plates_pack_01` and `_02`, the
"EXPEDITIONS" plates). A few have a plate texture of their own. Each bumper that carries a plate has
its own copy, so a truck with three bumpers has three plates in three places.

**Truck mods.** Every mod does it its own way. Some reuse the stock bumpers, plates included. Some
model a plate piece into their own body. Some have no plate at all.

## Why the plate is a cover

An add-on cannot hide part of another mesh. So the custom plate is a thin plate mesh that sits a few
millimetres in front of the stock plate and covers it. It has the same outline, faces the same way,
and has its edges folded back so it reads as one solid plate from the side.

That plate is an add-on like any other. It fits a **slot** on the truck and names the bumper it
belongs to:

```xml
<GameData Category="fender_front" Price="100">
    <RequiredAddon Types="harvester_scout_800_front_bumper_default" />
    <InstallSocket Type="LicensePlateHarvesterScout800" />
</GameData>
```

`RequiredAddon` makes the plate fittable only while its own bumper is on the truck. It works from a
mod's add-on to a bumper that came with the game. The other bumpers' versions are still listed in the
garage, but can't be fitted.

## One mesh, any number of plates

Converting a mesh needs the editor's converter for every model, which is slow. The plate avoids it.

A converted mesh starts with a small text header that names its textures:

```
AlbedoMap="trucks/platemaker_a__d.tga"
```

Each plate bumper is converted **once**, as a master. A new plate is a copy of that master with one
change: the texture name in the header now points at the new plate's own picture. The shape, the
mapping and everything else stay byte for byte the same. Only the plate picture itself goes through
the game's texture converter.

## Adding the slot

Trucks that came with the game keep their classes in the game's own `initial.pak`, and a mod cannot
add a slot to them. As with [rock lights](rock-lights.html), that needs a patcher on your own PC,
which is why the Plate Maker is PC only.

A truck mod keeps its classes in its own pak, and a mod's add-ons only work inside that same mod. So
on a mod truck, the slot and the plates go into that mod's own files. The slot copies the
`ParentFrame` and `Offset` of the slot its bumper fits in, so the plate sits where the bumper sits.

!!! warning "Mod updates"
    Updating a truck mod from mod.io replaces its paks, and its plates go with them. Put them back
    afterwards. If the update moved the bumper's slot, the plate would float, so the Plate Maker
    skips that truck instead.

## Which trucks

- **Trucks that came with the game:** 37 carry a plate on a front bumper. The Haukka NS420 has a
  full-size plate only on its standard bumper. Its other two bumpers show a 6.6 cm strip, too thin
  for a plate. On the Tatra T815-7 Force and the Shiba Overlander, the light-coloured parts that
  look like a plate are a long strip, a slanted panel and a grille. They are not plates.
- **Truck mods, measured on these mods in November 2026:** 12 NOA Scouts trucks (the stock bumpers
  they share), the RosenBug (its own rear plate piece), and the Jeep Pack RC CJ-7 where its version
  has a tail plate hanger or a tire-carrier plate.

## Sharing what you made

Changing a truck on your own PC is yours to do, whoever made it. **Uploading** someone else's truck
with plates added is not, unless its author says you may or its licence allows it.

The state plate designs belong to the states that issue them. The Plate Maker fetches them from
blanklicenseplates.com on your own PC and does not ship them.

## What has been checked

- In game: custom plates on the stock bumpers of trucks that came with the game (Scout 800, DON 71),
  with only the fitted bumper's version buyable.
- In game: one master mesh showing two different plates by changing only the texture name.
- In game: plates on the CJ-7's tail hanger and tire carrier.
- **Not yet checked in game:** the plates on the NOA Scouts trucks and the RosenBug.
