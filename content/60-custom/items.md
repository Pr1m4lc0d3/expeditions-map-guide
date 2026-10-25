---
title: Custom inventory items
part: Custom content
order: 620
status: draft
summary: Your own devices, tools and quest items, and the one flag that decides whether a mission using them can start.
---

# Custom inventory items

An inventory item is anything that rides in a truck's **Inventory** slots or
**Sideboard** (cargo) slots: tools like the anchor and jack screw, quest pickups
like a camera trap or a flight recorder, and valuables the player sells at the end
of a run. <span class="prov prov-doc">documented</span>

Items do one of two jobs:

- **Usable items** run a piece of built-in game logic when the player presses
  *Use*: place an anchor, lift the truck with a jack screw. You can only reuse
  logic the game already has, but you can retune its numbers.
- **Everything else** has no behaviour of its own. It exists to be found, carried,
  delivered, crafted, recycled or sold, and objectives give it meaning.

Fuel, repair parts and spare wheels are **not** inventory items and cannot be made
as one. Those are consumables, built as truck addons.
<span class="prov prov-doc">documented</span>

!!! note "What this page does and does not cover yet"
    The descriptor fields, item types, the HQ flag and the Workshop values are
    sourced from Saber's guide, the editor schema and item mods tested in game.
    Several things are **not yet known** and are marked where they come up:
    whether the four-mod HQ limit behaves as documented, whether `invId` is ever
    read, and every ability class except the jack screw.

## What an item mod contains

```
Documents\My Games\Expeditions\Media\Mods\
  InventoryItemDesc_<id>\
    InventoryItemDesc              the descriptor (JSON, no file extension)
    ui\textures\<name>_20.png      optional custom icons, see Icons
    ui\textures\<name>_30.png
    ui\textures\<name>_40.png
    ui\textures\<name>_60.png
  InventoryItemDesc_<id>.pak       what the game loads
```

Make one in the editor: **EXP MODs creation**, **File > New Mod > Inventory
Item**, type an id in **name**, choose the class in **InventoryItemDesc**, fill in
the fields, **File > Save**, **File > Pack**, restart the game.
<span class="prov prov-doc">documented</span> As with specialists, the first save
fails with `Can't open file` if `Media\Mods` does not exist yet; create it by hand.

### The id

The id is what objectives and loot zones use to refer to the item. Saber allows
only Latin letters, digits and underscores. <span class="prov prov-doc">documented</span>

Use underscores (`Like_This`), and do not count on spaces being tolerated. The
custom items confirmed working on the test install all have underscored ids. Whether
a space in an item id breaks anything has not been settled, but the game is known
to split some names on whitespace: a loot zone whose id contains a space cannot be
looted at all (see [Loot, storage and airdrops](../40-zones/storage-zones.html)).

## The class: what the item can do

The class you pick decides which ability logic the item gets, and which extra
fields appear.

| Class | For | Vanilla examples | Status |
|---|---|---|---|
| `InventoryItemDesc` | No ability: quest items, treasure, GPS tracker | Memory card, Dinosaur bone, Flight recorder | Works. Tested. |
| `InventoryItemDescJackScrew` | Lifts and re-places the truck | Jack screw | Works. Tested. |
| `InventoryItemDescAnchor` | A placeable winch point; also the signal amplifier | Anchor, Removable anchor, Signal amplifier | Documented. Not tested here in play. |
| `InventoryItemDescDrone` | Air drone | Drone | **Do not make.** Saber says it causes errors. |
| `InventoryItemDescEcholot` | Echo sounder | Echo sounder | **Do not make.** Saber says it causes errors. |
| `InventoryItemDescBinocular` | Binoculars | Binoculars | **Do not make.** Saber says it causes errors. |

Saber's warning against drone, echo sounder and binocular items promised a fix in
a later release. Support ended in September 2026, so the warning stands.
<span class="prov prov-doc">documented</span>

A usable item also needs `baseTypeAbility` set to the matching ability. The JSON
stores it as a number:

| Value | Ability | Value | Ability |
|---|---|---|---|
| `0` | `NONE` | `4` | `JACKSCREW` |
| `1` | `BINOCULAR` | `5` | `ECHOLOT` |
| `2` | `ANCHOR` | `10` | `DRONE` |
| `3` | `SIGNAL_AMPLIFIER` | | |

The schema lists more abilities after these (the drones, portable bridges, tow
rope and some obsolete test entries). Saber's guide covers only the ones above.
<span class="prov prov-schema">schema only</span>

## The general fields

Every class has these. The JSON below is a working quest item, trimmed to the
general fields:

```json
{
    "SslType": "InventoryItemDesc",
    "SslValue": {
        "name": "InventoryItemDesc",
        "type": 14,
        "baseTypeAbility": 0,
        "uiName": "My Item",
        "uiDesc": "One line for the inventory tooltip.",
        "icon20": "myitem_20", "icon30": "myitem_30",
        "icon40": "myitem_40", "icon60": "myitem_60",
        "iconDesc": null,
        "defaultUseCount": 1,
        "cost": 0,
        "craftRepairsCost": -1,
        "craftUseCount": 0,
        "recycleRepairsCost": -1,
        "isUsable": false,
        "isHeavyItem": false,
        "isTreasure": false,
        "canTakeInHq": false,
        "notForSale": true,
        "isRequired": false,
        "notForCoopDel": false,
        "notForDuplicate": false,
        "canBeUsedInCave": true,
        "hasIconOnMinimap": false
    },
    "name": "My_Item"
}
```

The top-level `name` is the item's id. `SslValue.name` is always
`"InventoryItemDesc"`.

| Field | What it does | Default |
|---|---|---|
| `type` | The item's category. See [Type](#type-the-category-everything-else-matches-on). | `BINOCULAR` (0) |
| `uiName` | Name in the UI. Saber's limit: 20 characters. | |
| `uiDesc` | Description. Saber's limit: 80 characters. | |
| `icon20` to `icon60` | The four icons. See [Icons](#icons). | |
| `defaultUseCount` | Charges. `-1` is unlimited. Quest and treasure items use `1`. | |
| `cost` | Price at Headquarters, whole number. | `0` |
| `craftRepairsCost` | Spare parts to craft it at a Workshop. `-1` means not craftable. | `-1` |
| `craftUseCount` | Charges a crafted copy comes with. | |
| `recycleRepairsCost` | Spare parts it recycles into at a Workshop. `-1` means not recyclable. | `-1` |
| `isUsable` | The player can press *Use* on it. `true` for ability items. | |
| `isHeavyItem` | Goes in the Sideboard (cargo slots), not Inventory. | `false` |
| `isTreasure` | Sold at the end of the expedition; sell-price specialists boost it. | `false` |
| `canTakeInHq` | Can be bought at Headquarters before a run. See below. | **`true`** |
| `notForSale` | Saber lists it as "TBD". Not tested. | `false` |
| `isRequired`, `notForCoopDel`, `notForDuplicate`, `canBeUsedInCave`, `hasIconOnMinimap` | Present in the schema and in working mods; not described by Saber, not tested here. | `false`, `false`, `false`, `true`, `false` |

The defaults are the editor schema's. Saber's limits on `uiName` and `uiDesc` are
not enforced everywhere: a tested custom item showed a 28-character name and a
150-character description in full in the Workshop panel. Whether longer text
breaks other screens has not been checked.

Rules from Saber's guide, all <span class="prov prov-doc">documented</span>:

- **`isUsable` and `isHeavyItem` do not mix.** A usable item can only be used from
  Inventory or the radial menu, never from the Sideboard. Heavy items that are
  only delivered (a radio station, say) are fine.
- **`isTreasure` and `canTakeInHq` together crash the game.** Treasure cannot be
  sold at HQ.

!!! danger "`canTakeInHq` defaults to true"
    The schema default for `canTakeInHq` is `true`. A treasure item left on the
    default therefore carries the crashing combination. Set `canTakeInHq: false`
    on every treasure item, as the tested treasure mod does.

## Type: the category everything else matches on

Every item has a `type` from a fixed list. Anchor and Removable anchor are
different items with the same type. Type does not change how the item behaves; it
is a **tag**, and objectives and loot zones usually refer to items by type rather
than by id. <span class="prov prov-doc">documented</span>

So any item with the right type satisfies a requirement for that type. Saber's
example: a delivery stage that asks for a type accepts *any* item of that type.
<span class="prov prov-doc">documented</span>

!!! warning "Give items you need to tell apart different types"
    Objectives, loot slots and required-inventory lists have an id field
    (`invId`, `itemName`) as well as a type. Saber's guide marks the id field in
    `takeInventory`, `objectConstruction` and required inventory as "currently not
    added" or "not implemented", and support ended without it being finished.
    <span class="prov prov-doc">documented</span>

    Whether the game reads it anyway is **not established**. The safe assumption
    is that only `type` counts. If two of your items must not be mistaken for each
    other (two different quest pickups, say), give them different types.
    The large list of quest types exists for this.

The JSON stores `type` as a number, its position in the schema's list. These
values are confirmed against working items in shipped or tested data:

| Value | Type | Confirmed by |
|---|---|---|
| `4` | `ANCHOR_SETUP` | vanilla `Anchor` in a loot zone |
| `5` | `JACK_SCREW` | vanilla `Jack_screw` in a loot zone |
| `14` | `QUEST_ITEM` | a tested custom quest item |
| `44` | `TREASURE` | vanilla `Arizona_Treasure_1` |
| `45` | `SCRAP_FOR_WARKSHOP` | vanilla `Scrap_For_Workshop` |

By counting the same list, `QUEST_SUPPLIES` is `24`; that one has not been checked
against a working item.

!!! warning "Count from zero, and check before you trust an index"
    The list starts `BINOCULAR` = `0`, `DRONE` = `1`. In the schema file the
    default value is printed above the list, so a quick scrape comes out **off by
    one**. Check any new index against a known item before relying on it.

Saber's appendix lists every vanilla type with what it is used for. Quest types
include `AMULET`, `ANIMAL_TRAIL_CAMERA`, `BATTERY`, `CANDLES`, `DINO_BONE`,
`EQUIPMENT_BOX`, `FISH`, `GOLD_PRILL`, `MAP`, `MEMORY_CARD`, `MUSHROOMS`,
`QUEST_ITEM` (the universal quest type), `QUEST_SUPPLIES`, `RADIO_STATION`,
`VIDEO_CAMERA`, `WATER_ANALYZIS` and more. `NONE`, `FUEL_CANISTER`, `TOOLKIT` and
`PENALTY_ITEM` are unused.

Vanilla item ids worth knowing, for loot zones and objectives:

| Id | Type |
|---|---|
| `Anchor` (removable), `Anchor_not_removable` | `ANCHOR_SETUP` |
| `SignalAmplifier` | `SIGNAL_AMPLIFIER_SETUP` |
| `Jack_screw`, `Jack_screw_strong` | `JACK_SCREW` |
| `GPS_Tracker` | `GPS_TRACKER` |
| `Scrap_For_Workshop` | `SCRAP_FOR_WARKSHOP` |

## The Headquarters flag

`canTakeInHq` decides whether the player can buy the item at **Headquarters**
while preparing an expedition.

!!! danger "An expedition that requires an item without this flag can never start"
    If an expedition's **Required inventory** lists an item, that item must be
    available at Headquarters, so a custom item there must have
    `canTakeInHq: true`. Otherwise the player cannot load it, cannot meet the
    requirement, and the expedition refuses to start without explaining why.
    <span class="prov prov-doc">documented</span>

    Required inventory is for expeditions only, not contracts or tasks.
    <span class="prov prov-doc">documented</span>

Headquarters has 16 inventory slots and 16 sideboard slots, shared between
vanilla and modded items. Saber gives a limit of **4 enabled item mods** with
`canTakeInHq: true` for inventory items, and 4 for sideboard items, counting local
paks and mod.io subscriptions together. Past the limit, some of them silently drop
off the HQ lists. Disable some in the Mod browser, or delete local test paks you
no longer need. <span class="prov prov-doc">documented</span> Not tested here.

## Icons

Each item names four icons:

| Field | Size | Where it shows |
|---|---|---|
| `icon20` | 20 x 20 | Requirements at Headquarters |
| `icon30` | 30 x 30 | Summary and specialist screens |
| `icon40` | 40 x 40 | The map |
| `icon60` | 60 x 60 | The inventory slot |

<span class="prov prov-doc">documented</span>

There are two ways to fill them.

**Borrow a vanilla icon.** Put the name of a game icon in each field. Saber's
appendix lists them; most differ only in the size suffix:

```
toolAnchorImg20 / 30 / 40 / 60            Anchor
toolAnchorAlternateImg20 ...              Removable anchor
toolJackScrewImg20 ...                    Jack screw
toolDroneImg20 ...                        Drone
objectivesQestItem20 ...                  most quest items
toolToolkitImg20 ...                      QUEST_ITEM type
scrapForWorkshop_20 / _30 / _40 / _60     Scrap for Workshop
treasureArizona1_20 ... treasureCarpathians3_60   the six treasures
```

The one irregular name: Portable rig part uses `toolPortativeDrillImg20/30/40` but
`toolAddonDrillImg60`.

**Ship your own PNGs.** Saber's guide says custom item icons are not supported.
The test install says otherwise: item mods that ship
`ui/textures/<name>_20.png` through `_60.png` at the four sizes, as RGBA, and name
them in the fields without folder or extension, show their own icons in game.
<span class="prov prov-unver">measured on one install</span>

!!! warning "A named icon that is not in the pak renders blank"
    If a field names an icon and the pak carries no file of that name (and it is
    not a vanilla icon name), the slot is simply empty. An early build of a tested
    item named its four icons and shipped no textures, and showed an empty
    slot. Save icons as RGBA, not palettised.

`iconDesc` cannot be customised. <span class="prov prov-doc">documented</span>

## Crafting and recycling at the Workshop

A [Workshop](../62-modules/workshop.html) turns spare parts into items and items
into spare parts. An item is **craftable** when `craftRepairsCost` is not `-1`, and
**recyclable** when `recycleRepairsCost` is not `-1`. The two are independent.
<span class="prov prov-doc">documented</span>

A tested custom jack-screw item with `craftRepairsCost: 1000` appeared in the
Workshop's craft list, with its own name and description, and showed "Not enough
spare parts: 1000" until the Workshop held enough.

The vanilla values, for pricing your own:

| Item | Recycles into | Costs to craft |
|---|---|---|
| Scrap for Workshop | 50 | not craftable |
| GPS tracker | 50 | 220 |
| Big portable bridge | 70 | 150 |
| Small portable bridge | 40 | 100 |
| Signal amplifier | 40 | 160 |
| Fixed anchor | 40 | 160 |
| Jack screw | 40 | 200 |
| Tow rope | 20 | 50 |

Recycling pays well under the craft price everywhere in vanilla. An item that
recycles for more than it crafts for turns the Workshop into a spare-parts
machine.

## Ability items

These fields appear only on the ability classes.

### Jack screw: `InventoryItemDescJackScrew`

Tested. A custom jack-screw item with the fields below let the player pick the
truck up and set it down on a ledge well above it.

| Field | What it does | Tested value |
|---|---|---|
| `radius` | How far from the truck it can be re-placed, meters | `30` |
| `useIfRolledOverOnly` | Only usable on a rolled-over truck. Saber: on by default. | `false` |
| `jackScrewControllerDesc.modelSetupPreviewControllerDesc.height` | Highest placement relative to the truck | `30` |
| `...maxUserDefinedHeight` | How high the player can lift the preview | `30` |
| `...allowSetupUnderWater`, `...allowedWaterLevel` | Placement in water, and the deepest allowed | `true`, `0` |
| `...rotationSpeedModifier` | Rotation speed of the preview | `5` |
| `...doPaintModel` | Tint the preview green or red. Saber recommends leaving it on. | `true` |

Set `baseTypeAbility: 4`, `type: 5` (`JACK_SCREW`), `isUsable: true`. Saber's
guide spells the rolled-over switch `uselfRolledOverOnly`; the schema's name is
`useIfRolledOverOnly`.

The vanilla jack screw is meant to right a rolled truck. Turning off
`useIfRolledOverOnly` and raising the radius and heights makes it a short-range
teleport, which is a large gameplay change; price it accordingly.

### Anchor: `InventoryItemDescAnchor`

Documented by Saber; a custom anchor exists on disk but has not been tested here
in play. Main fields: `setupRadius` (meters), `controllerDesc` (an
`AnchorSetupControllerDesc`) holding `anchorBrand` (`test_anchor` for the vanilla
model), `previewAnchorModel` (`models_test_anchor`), `isRemovableByWinch` (`true`
on the removable anchor), `upDirOffset`, `scale`, and the same placement preview
block as the jack screw. <span class="prov prov-doc">documented</span>

!!! warning "Custom anchor models are not supported"
    Saber's guide describes how a custom anchor model would be set up
    (`NeedPreload="true"` on the model class and a `<WinchSocket Pos=...>` in its
    `GameData`) and then says custom anchor models are not supported. Use the
    vanilla model. <span class="prov prov-doc">documented</span>

A **signal amplifier**, which gives wheeled drones a signal zone, is an anchor-class
item with `type` `SIGNAL_AMPLIFIER_SETUP` and ability `SIGNAL_AMPLIFIER`. Its radius
is set in the model's XML (`SignalRadius="100.0"`), not in the item. Saber points to
`signal_amplifier_dlc06.xml` as the example. <span class="prov prov-doc">documented</span>
Not tested here.

### GPS tracker

A plain `InventoryItemDesc` with `type` `GPS_TRACKER` and no extra fields. Saber:
items in the inventory are sold when the expedition is completed.
<span class="prov prov-doc">documented</span> Not tested here.

## Using your item in a map

Your item reaches the player in three ways: bought at **Headquarters**
(`canTakeInHq`), found in a **loot zone** on the map, or **crafted** at a Workshop.
<span class="prov prov-doc">documented</span>

**As loot.** A `ZonePropertyInventoryStorage` zone lists possible items per slot,
each with a `type`, a `chance` from `0` to `1`, and an optional `itemName`:

```json
{ "$type": "ZoneItem", "chance": 1.0, "itemName": "My_Item", "type": 14 }
```

Set the zone's `capacity` above `0` or nothing shows, and give the zone an id with
**no spaces** or the player cannot take anything from it. See
[Loot, storage and airdrops](../40-zones/storage-zones.html).

**As something to collect or deliver.** A `takeInventory` stage asks the player to
pick items up from a zone; an `objectConstruction` stage asks them to bring items
to one. Both name the item by `type` (and an id field that may not be read, see
above). See [The assignment types](../50-missions/assignment-types.html).

**As a requirement or a reward.** List it in an expedition's Required inventory
(and set `canTakeInHq`), or hand it over with `ObjectiveRewardItem`. See
[Rewards](../50-missions/rewards.html).

**As a quest item with a visible result.** Saber's camera trap is only a name, an
icon and a description. Delivering it to a construction zone switches an
`_objective` model on the map to its built state, which is what shows the camera
on the tree. <span class="prov prov-doc">documented</span>

## Not yet known

- Whether `invId` / `itemName` in objectives and required inventory is read at
  all. Assume not.
- Whether a `QUEST_ITEM` is accepted as a construction-zone requirement. Every
  shipped example uses consumable types.
- The four-mod HQ limit, in practice.
- What `notForSale`, `isRequired`, `notForCoopDel`, `notForDuplicate`,
  `canBeUsedInCave`, `hasIconOnMinimap`, `canBeUsedFromDrone` and
  `setupRadiusCoefficient` do.
- The schema's other abilities (portable bridges, tow rope, the drone spawners).
- Heavy (sideboard) custom items, and custom inventory or cargo slots on trucks.
