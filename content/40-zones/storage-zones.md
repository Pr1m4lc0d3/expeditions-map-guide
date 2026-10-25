---
title: Loot, storage and airdrops
part: Zones
order: 430
status: draft
summary: Zones that hold things the player can take, and the naming rule that silently breaks all of them.
---

A storage zone is a zone holding things the player can move into a truck: inventory
items, fuel, repair parts and spare wheels. Air drops, loot caches, quest item
stashes and the Base module are all the same property,
`ZonePropertyInventoryStorage`. <span class="prov prov-doc">documented</span>

!!! danger "Read the naming rule first"
    A zone whose Id contains a **space** can never be looted. The items appear, the
    trade screen opens, you press move, and nothing arrives, with no error at all.
    The game splits its internal reference to the zone on whitespace and then looks
    up the wrong name. Verified in game, September 2026: renaming one zone to use
    underscores fixed it immediately. The full story is on
    [Where everything lives](../00-start/where-things-live.html#zone-names-spaces-in-the-source-underscores-in-the-pack).

!!! note "What on this page has been tested"
    Taking random air drop loot from a zone with a correct Id works in game, and so
    does the consumables slot behaviour described below. Custom (non-random) loot,
    `additionalLoot`, the specialist perk switches and what survives between
    expeditions have **not** been tested by this guide, and are labelled.

## The settings

### How much it can hold

| Field | What it does |
|---|---|
| `capacity` | number of slots for ordinary items |
| `heavyInvCapacity` | number of slots for heavy items |

Both default to **0**, and a storage with `capacity` 0 shows no inventory at all,
even when its items are set up correctly. <span class="prov prov-doc">documented</span>
Changing it is the first thing to do.

Slots you do not fill with items stay empty, and the player can use them to unload
things from the truck. If you list more item slots than the capacity allows, the
list is cut down to fit. <span class="prov prov-doc">documented</span>

### What can appear in it

`slotsSettings` is a list of slots. Each slot has a list of `possibleItems`, and
each possible item has:

| Field | What it does |
|---|---|
| `type` | the kind of item. See [Custom inventory items](../60-custom/items.html) |
| `chance` | the probability it appears, from `0` to `1` |
| `itemName` | optional. Picks one specific item where several share a type |

`chance` is a plain probability: `0.75` is 75%, and **`1` means always**. It
defaults to **0**, so an item you add and forget to set will never appear.
<span class="prov prov-doc">documented</span>

Saber advises that at least one slot's chances should add up to `1`. Otherwise the
zone can spawn with nothing in it. <span class="prov prov-doc">documented</span>

### Fuel, repair parts and wheels

These are not item slots. Each has its own block: `fuelSlotSettings`,
`repairsSlotSettings` and `wheelsSlotSettings`.

| Field | What it does |
|---|---|
| `quantity` | how much is there |
| `chance` | probability it appears, `0` to `1` |
| `tradeFromTruckToZone` | whether the player may move this resource **from the truck into the zone** |

`tradeFromTruckToZone` controls only that one direction, truck to zone. It does not
switch off taking from the zone. Tested in game, October 2026.

!!! note "Can't be transferred usually means the truck is full"
    When taking spare parts from a storage shows a red "Can't be transferred", the
    usual cause is that the truck has no room left for them. Check the truck before
    suspecting the zone. Tested in game, October 2026; see
    [Repair station](../62-modules/repair-station.html).

### The other switches

| Field | What it does |
|---|---|
| `alwaysSpawn` | appear in every expedition. Off means the zone joins the random draw, see below |
| `isAtDeployZone` | **only** for the Base module's storage on a deploy zone. Off everywhere else |
| `isAffectedByAdditionalAirdropResourcesAbility` | specialist perks that add air drop fuel, parts and wheels apply here. Saber: usually on for air drops |
| `isAffectedByAdditionalOutpostResourcesAbility` | the equivalent outpost perks apply. Saber: usually on for FOB modules |
| `model` | optional model that is visible only while this zone is spawned, for example a crate pile at an air drop. See [Construction zones](construction-zones.html#making-something-appear) for how models change state |
| `zoneDiscoverability` | whether the player can see the zone yet. See [Hiding and revealing zones](discoverability.html) |
| `expandedConsumablesCapacity` | Saber says this does not work as described yet. Leave it alone |

<span class="prov prov-doc">documented</span> The two perk switches are
<span class="prov prov-unver">unverified</span> in game.

## Air drops: random by design

At the start of each expedition the game decides which air drops exist and what is
in them. <span class="prov prov-doc">documented</span>

<div class="step"><div class="n">1</div><div>

**Which zones spawn.** Every storage zone with `alwaysSpawn` **off** goes into a draw.
The game spawns only as many as `maxInventoryZones` allows. You set that number in
Zone Settings, in the map's `inventorySettings` section.

</div></div>

<div class="step"><div class="n">2</div><div>

**What is in each one.** Inside a zone that spawned, each item and each consumable
appears according to its own `chance`.

</div></div>

<div class="step"><div class="n">3</div><div>

**Extra items.** `inventorySettings` also has an `additionalLoot` list. Each entry,
given by `type` and optionally `itemName`, is added to one of the zones that
spawned, on top of its random contents. <span class="prov prov-unver">unverified</span>
in game.

</div></div>

So place more air drop zones than `maxInventoryZones`, and every expedition on the
map gets a different set. Air drop locations and contents are drawn again for each
new expedition. <span class="prov prov-doc">documented</span>

A zone that must always be there, such as a quest stash, gets `alwaysSpawn` on and
stays out of the draw.

## Specific loot instead of random

To guarantee what a zone holds, give it `alwaysSpawn` on, one slot per item, one
possible item per slot, and `chance` set to `1`. Use `itemName` when the item shares
its type with others, as the Anchor and the Removable Anchor do.

<span class="prov prov-unver">unverified</span> Fixed loot built this way follows
directly from the documented fields, but it has not been taken from a zone in game by
this guide.

!!! warning "Only `type` is known to be read in objectives"
    The item-id fields on the `takeInventory` and `objectConstruction` objectives are
    marked by Saber as not yet added, so those objectives match items by `type` only.
    If an objective must tell two of your items apart, give them different types.
    Whether a storage slot's `itemName` is honoured is a separate question, and is
    untested here.

## What survives between expeditions

Items the player leaves in a storage zone are normally gone next expedition. Saber's
expeditions page names one exception: items the player puts in the **Warehouse**
(`EXTRA_STORAGE`) are still there next time. <span class="prov prov-doc">documented</span>

Saber's storage page also says that `isAtDeployZone` saves items in the Base module.
The two pages do not agree, and neither has been tested here.
<span class="prov prov-unver">unverified</span>

## Storage at a base module

The Gas station, Repair station, Warehouse, Essentials storage and Base module are all
storage underneath, wrapped in `ZonePropertyFobModuleStorage`. That wrapper belongs in
a custom module's descriptor, **never on a zone you place**. Saber warns it may crash
the game on an ordinary zone. To shape a module's stock, see
[Module descriptor reference](../60-custom/base-modules-reference.html#shaping-a-storage-module).

## Checklist

- the zone's Id has **no spaces**, in the packed map
- `capacity` (and `heavyInvCapacity` if needed) is above 0
- every `chance` you meant to be non-zero is set, and at least one slot adds up to `1`
- `alwaysSpawn` is on for anything that must always exist, off for air drops
- `maxInventoryZones` is set, and is smaller than the number of air drop zones
- `isAtDeployZone` is off unless this is the Base module
