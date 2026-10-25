---
title: Construction zones
part: Zones
order: 440
status: draft
summary: Zones where delivering materials makes something appear, which is how bridges get built.
---

A construction zone is a place the player delivers materials to, after which
something appears on the map: a bridge, a camera trap on a tree, a radio station.
There are two ways to set one up, and they share almost everything.

| | A construction **zone** | A construction **assignment** |
|---|---|---|
| What you add | `ZonePropertyObjectConstructionInZone` on a zone | an `objectConstruction` substage in an objective |
| Needs an objective | no. The player finds the zone, delivers, and it builds | yes |
| Where the delivery is set | `requiredItems` in the prop | each record of `zoneToFill` |

<span class="prov prov-doc">documented</span>

!!! warning "Nothing on this page has been tested in game by this guide"
    Everything here is from Saber's guides. Several of the fields involved are
    marked by Saber itself as not implemented or not finished, and that is said
    where it applies. Treat this page as a map of the documented fields, not as a
    proven recipe, until it has been tested.

## Without an objective: the construction property

Give a zone `ZonePropertyObjectConstructionInZone` and it waits for a delivery. When
the **last** required item arrives, the model it is linked to changes state.
<span class="prov prov-doc">documented</span>

| Field | What it does |
|---|---|
| `requiredItems.repairsNum` | repair parts required |
| `requiredItems.fuelNum` | fuel required |
| `requiredItems.inventory` | required items. **Saber marks every field inside this as not implemented** |
| `model` | the model that changes state when the delivery is complete. See [below](#making-something-appear) |
| `modelPlacementZones` | zones that block the delivery while a truck is in them |
| `additionalConstructionZones` | other zones that accept the same delivery and build the same model. Saber marks this "TBD" |
| `zoneDiscoverability` | whether the player can see the zone yet. See [Hiding and revealing zones](discoverability.html) |
| `uiDesc` | does nothing. Saber says it will be removed |

So by Saber's own account, the property is only known to be usable for **fuel and
repair parts**. A construction that needs a specific item belongs in an objective.

Do not confuse this with `ZonePopertyObjectConstruction` (Saber's spelling), its
parent. That one is an internal prop the game adds itself to the targets of
`objectConstruction` assignments. Do not add it by hand.

## With an objective: `objectConstruction`

The same idea, driven by an assignment, is covered on
[The assignment types](../50-missions/assignment-types.html#objectconstruction). In
short, each `zoneToFill` record names a target zone in `globalZoneId` and what to
deliver there:

- `repairsNum`, `fuelNum`, and `inventory` (a `Type` and an `Amount`). At least one
  must be set
- **Model Building Settings (Depend On Cargo)**, the model that appears when this
  delivery is done
- `additionalUnloadZones` and `modelPlacementZones`, described below

The item-id field inside `inventory` is marked by Saber as "currently not added", so
items are matched by `Type` alone.

## Making something appear

Both versions use **Model Building Settings**: a model on the map switches from one
named state to another, playing its animation if it has one.
<span class="prov prov-doc">documented</span>

<div class="step"><div class="n">1</div><div>

### Pick a model that has states

Only models already set up with states can do this. Their names end in
`_objective`, so search for that suffix in the editor's Select Asset window. Saber's
example is `animal_tracking_camera_01_objective`.

</div></div>

<div class="step"><div class="n">2</div><div>

### Find the state names

Open the model's class XML in `initial.pak`, under `[media]\classes\models\` (or the
same path inside `[media]\_dlc\`). Each `<Subset Name="...">` is one state. For the
camera trap they are `build_stage_0`, the bare tree, and `build_complete`, the trap
installed.

</div></div>

<div class="step"><div class="n">3</div><div>

### Tag the model

Place the model and give it a **Tag** in its properties in the editor. The settings
find the model by that tag.

</div></div>

<div class="step"><div class="n">4</div><div>

### Fill in the settings

| Field | What to put |
|---|---|
| `levelName` | your map's name, without `.xml` |
| `modelTag` | the tag from step 3 |
| `stagesProgress` | two entries: the "not delivered" state at `0`, the "delivered" state at `1`. Names exactly as in the XML |
| `unloadBlockedZoneId` | optional zone that blocks unloading while a truck is in it |
| `modelType` | meant to pick a sound for the change. Saber says it does not work as intended |

</div></div>

!!! warning "State names cannot contain spaces"
    Saber's guide says names of model states must be written without spaces, or
    they will not work. <span class="prov prov-doc">documented</span>

!!! warning "One `_objective` model, one delivery"
    Do not use the same `_objective` model in two separate delivery stages. If a
    model should depend on two deliveries, link it to the objective's completed
    stages instead, with **Model Building Settings (Depend On Stages)** on the
    objective. <span class="prov prov-doc">documented</span>

A prop named `ZonePropertyModelAnimationTrigger` is also documented as a way to
change a model's state from a zone without any objective, set up "similarly to
`objectConstruction`". Saber gives no further detail.

## Bridges from either bank

A river crossing is the case these zones were built for. A player arriving from
either side should be able to build the bridge.

- In an **assignment**, list the zone on the far bank in `additionalUnloadZones`. A
  delivery to either zone counts. Saber says the base game used this for bridges.
  <span class="prov prov-doc">documented</span>
- In a **construction zone**, the matching field is `additionalConstructionZones`,
  which Saber marks "TBD". <span class="prov prov-unver">unverified</span>

## Keeping trucks out of the way

When the model appears, a truck parked where it appears would be clipped into it.
`modelPlacementZones` lists zones that block the delivery, and the build, while any
truck is inside one of them. Cover the footprint of the model with one, and the
player has to move clear before the bridge appears.
<span class="prov prov-doc">documented</span>

## These zones move items, so the naming rule applies

A delivery passes items through the zone, so its Id must not contain a space. The
space bug is proven in game for **taking** items out of a zone; that delivering
into one fails the same way is <span class="prov prov-unver">unverified</span>, but
there is no reason to risk it. Use underscores. See
[Where everything lives](../00-start/where-things-live.html#zone-names-spaces-in-the-source-underscores-in-the-pack).

## What is not known yet

- whether `requiredItems.inventory` on the construction property does anything
- whether `additionalConstructionZones` works
- how `ZonePropertyModelAnimationTrigger` is configured
- the whole chain tested end to end in a running game
