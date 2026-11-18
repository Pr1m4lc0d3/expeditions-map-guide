---
title: Add-on slots, dependencies and gear
part: Vehicles
order: 673
summary: How a new part reaches the garage. Slots on the truck, requirements on other parts, supply gear that adds fuel and spare parts, and the quiet failures between them, from a frame name ending in .001 to a socket offset the game ignores.
status: draft
---

# Add-on slots, dependencies and gear

A part you have built is not in the game until the truck has a slot for it and the part knows which
slot it fits. [Rock lights on any truck](rock-lights.html) walks through the basic mechanism with a
complete example. This page collects what goes wrong once a truck has many add-ons that depend on
each other: a rack, gear on the rack, a tent instead of the gear, a lift kit that changes the truck.

## Slots and requirements

- The **slot** is a `<Socket Names="...">` in the truck's `<AddonSockets>`. An add-on fits one with
  `<InstallSocket Type="...">`.
- Sockets listed together in one `<AddonSockets>` group are **one choice**: fitting one add-on
  clears the others. Put a tent and the gear that would sit in its place in one group, and the
  player picks one.
- An add-on that bolts onto another add-on needs `<RequiredAddon Types="a, b" />` before its
  `InstallSocket` (any one of the listed add-ons will do). Without it, the garage offers fender
  flares on a truck with no fenders under them, and they float.
- Ask "what does this bolt to?" for every new part, and write the requirement in the script that
  builds the part, not by hand in the pak. Hand edits are lost on the next build.

!!! warning "An add-on's own Offset is ignored"
    `InstallSocket` takes an `Offset`, and it looks like the way to slide a stock part (a drone
    carrier, the metal detector) onto your rack. In game it did nothing: the detector sat on the
    ground in front of the truck. Put the offset on the **truck's** socket instead
    (`<Socket Names="..." Offset="(x; y; z)">`). That worked, and the detector sat on the rack.

## The frame name trap

An add-on's class names the mesh frame it draws (`MeshFrame`) and the frame it rides
(`ModelFrame`). If Blender exports several add-ons in one session, it renames a reused helper
object `Bone_cdt.001`, then `.002`. The converted mesh then carries `BoneRackSlot1_cdt.001` while
the class asks for `BoneRackSlot1_cdt`, and the part does not appear. The XML looks perfect.

When an add-on "does not work" and its XML matches a working one, list the frames in its converted
mesh first. A script that exports many add-ons in one Blender session must delete its helper objects
after each export, not just unlink them.

## Mesh and class traps

These each cost a round trip into the game, and none of them reports an error.

- **Never point a mod class at another truck's mesh.** A gear class that reused a stock truck's
  tuning mesh (with its frames and a socket offset) **froze the game at the loading screen**: no
  log, no crash dump, nothing in the script callstack. Removing only that class let it load. Copy the
  shape you need into your own mesh instead. A mod mesh may still *name* the game's own textures.
- **Add-on meshes are placed from the truck's zero**, not from the socket's frame. One hardtop built
  relative to the chassis bone drew a metre too low, inside the cab, and looked for a day as if it
  did not draw at all.
- **Every add-on mesh needs the usual frames**: a `RootNode`, a `cdt` collision frame, then the
  mesh. One roll cage listed in the garage with a price but could not be bought and did not draw;
  its meshes lacked the frames every working add-on has. Adding them is the fix we use now.
- **A texture with alpha must be saved with alpha.** A `__d_a` texture written as plain RGB drew
  a banner as a white strip.
- **Another mod's classes resolve only inside that mod.** The game files every mod class under its
  mod's id, so a truck that names another mod's wheel set in `CompatibleWheels` never finds it. Copy
  the wheel classes, meshes and textures into your own mod. Then keep each tyre's inner sidewall
  where the truck's own tyre's is: borrowing another truck's wheel offset put one set of tyres
  16 cm too far in, with the hubs through the wheel faces.
- **Engines, gearboxes and suspensions take no requirements.** Only add-ons accept `RequiredAddon`
  or `RequiredSuspension`. "This lift needs the V8" cannot be enforced; the parts stay separate.
- **A dented corner may be the game, not your mesh.** Trucks take visual damage. Almost every stock
  add-on, and many stock trucks, set `AcceptVisualDamage="false"` on their `PhysicsModel`. Compare a
  garage shot before hunting for a fault in a mesh that looks crumpled in the field.

## Supply gear

Parts that carry supplies (fuel cans, a parts case, batteries, a tent with camp kit) are add-ons
whose `<TruckData>` adds capacity:

```xml
<TruckData FuelCapacity="45" RepairsCapacity="150" ElectricChargeCapacity="15" />
```

`<TruckData>` on an add-on accepts only a short list of fields: fuel, water, repairs, wheel repairs,
electric charge, the metal detector, radar, wheel drone, cistern and kung flags. Anything else is
ignored. That is why some things cannot follow a part: the engine ghost, for one, is read only from
the truck ([Placing the engine ghost](engine-ghost.html)).

Gear that is used up (`IsConsumable="true"`) can hide its mesh as it empties, with `FuelHide`,
`RepairsHide` and similar elements naming a frame and a threshold.

## When the truck itself changes

- **A lift kit** is a suspension set, and a suspension set can swap the whole truck for a **truck
  replacement** (`TruckReplacement` on the set, a class in `classes/truck_replacements/`). The
  replacement can carry its own axles, drive shafts, engine ghost and wheel track. Stock
  replacements carry almost none of the base truck's add-on sockets, and they do not need to:
  add-on sockets come from the base truck.
- **Big tyres need the lift.** `MaxWheelRadiusWithoutSuspension` on the truck's suspension socket
  locks tyres above that radius behind any suspension set other than the default.
- **A spare cannot follow the fitted tyres.** A spare-wheel add-on draws a fixed mesh, and
  `RequiredAddon` resolves only against add-ons, not wheels. Offer one spare per tyre size and let
  the player pick.

## Never pull a class a save is using

A save stores every fitted mod add-on as `<class>_<mod id>`. Remove that class from the mod and the
save names something that no longer exists. Before a rebuild drops any add-on class, scan the saves
(read only) and keep every fitted class, with its mesh and texture, until the player has taken the
part off in the garage.

## What has been checked

Confirmed in game on a built truck or a port: the socket offset, requirements, supply capacities,
the per-size spares, the loading-screen freeze and its fix, the hardtop drawn a metre low, and other
mods' wheel sets once copied in. The `TruckData` field list was read from the game's executable. The
frame-name fault was found by reading the converted meshes; the parts drew once the names matched,
but that fix was not checked on its own. Not yet confirmed: that the missing frames alone stopped the
roll cage, that the alpha flag alone fixed the banner, whether `AcceptVisualDamage="false"` keeps a
custom truck's body clean, and gear hiding as it empties on a custom part.
