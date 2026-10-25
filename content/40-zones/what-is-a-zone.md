---
title: What a zone is
part: Zones
order: 410
summary: A zone is a shape in the world plus a set of properties, and those two halves live in two different programs.
---

Read this before the other zone pages. A zone is two things that get edited
separately, and once you see the split, most zone problems explain themselves.

## Two halves, two programs

Saber's guides describe every zone as a **zone locator** plus its **props**.
<span class="prov prov-doc">documented</span>

| Half | What it is | Where you edit it | Where it is saved |
|---|---|---|---|
| **The locator** | The shape: where the zone is, how big, which way it faces, what it is called on screen | The map editor itself, in the properties panel after selecting the zone | `_zones.xml` or `subgroups\Zone_<name>.xml` under `Media\prebuild\<level>\` |
| **The props** | The behaviour: what the zone *does* | The **Zone Settings** plugin, opened from the editor's toolbar | `zone_settings.json` under `Media\levels\<level>\` |

A locator on its own does nothing in game. A zone with an empty props list is only
a named area, and Saber notes it will not be visible in the game until something
refers to it, such as an objective. <span class="prov prov-doc">documented</span>
That is not a fault. Many zones exist only so an objective has a place to point at.

## Adding one

<div class="step"><div class="n">1</div><div>

### Place the locator

In the editor, right-click the terrain (or the **Zones** section of the Scene View)
and choose **Add Zone**. It appears as `no_id`. Move it where you want it, then set
its **Id** in the properties panel. Save the map.

</div></div>

<div class="step"><div class="n">2</div><div>

### Give it props

Open **Zone Settings** from the toolbar. Expand your map, then
**TERRAIN LOCATORS LIST**, then your zone. Click the plus next to **props**, pick a
property type, fill in its fields, and save with Ctrl+S.

</div></div>

<div class="step"><div class="n">3</div><div>

### Pack and test

A map only loads with at least one expedition and one deploy zone, so you need
those before you can test any other zone. See
[Make a map that loads](../00-start/map-that-loads.html).

</div></div>

## The Id is the only link between the halves

The Zone Settings plugin lists your zones under **TERRAIN LOCATORS LIST** by their
Id, and that is how it matches a set of props to a locator in the scene.
<span class="prov prov-doc">documented</span> There is no other connection. If the
two names differ by one character, the props belong to nothing, and the zone you
placed has no behaviour.

This is where most zone problems actually come from: a capital letter, a stray
space, a rename on one side but not the other. When a zone "does nothing", compare
the two names character by character before you look at anything else.

Saber's rule for the Id is **lowercase Latin letters, digits and underscores only**,
for example `test_zone_01`, and no spaces. <span class="prov prov-doc">documented</span>
Follow it from the first zone you place. A space in the Id is harmless for a plain
deploy point but breaks any zone that items pass through, as explained on
[Where everything lives](../00-start/where-things-live.html#zone-names-spaces-in-the-source-underscores-in-the-pack).

The **Name** field on the locator (`UiName` in the file) is separate from the Id.
It is what the player reads, so it can be a proper title.

!!! warning "Zones do not work inside References"
    Saber's guide says zones can be added to a Reference, but will not work
    correctly on the map that the Reference is placed into.
    <span class="prov prov-doc">documented</span> Place zones directly on the map.

## One zone, several props

Props combine. A single zone can carry several property types at once, and each one
adds a function. <span class="prov prov-doc">documented</span> Saber's example is the
typical deploy zone, which carries three:

- `ZonePropertyDeploy`, so trucks can arrive there
- `ZonePropertyInventoryStorage`, for the Base module's storage
- `ZonePropertyRecovery`, so trucks can be recovered to it

So "a deploy zone that is also a store" is one zone, not two zones on top of each
other. Props can also be added to or removed from a zone during play, as an
objective reward. See [Rewards](../50-missions/rewards.html).

## The locator fields worth knowing

| Editor field | In the file | What it does |
|---|---|---|
| Org X, Org Z | `Org` | position on the map, in metres |
| Dir | `Dir` | the direction the zone faces, drawn as a purple arrow |
| Id | `Id` | the link to Zone Settings, see above |
| Name | `UiName` | the name the player sees |
| Is Visible On Minimap | `IsVisibleOnMinimap` | hides or shows the zone on the in-game map |
| Shape Type | `ShapeType` | rectangle or circle |
| Length or diameter, Width | `LengthDiameter`, `Width` | size in metres |
| Is Wall, Height | `IsWall`, `Height` | raise the zone above the surface instead of lying on it |
| Icon 30x30, Icon 40x40 | `Icon30x30`, `Icon40x40` | leave empty, see below |
| Distributions group name | `DistributionGroupName` | SnowRunner only. Not used in Expeditions |

!!! note "Leave the icon fields empty"
    Expeditions assigns zone icons automatically from the zone's props and the
    objectives that use it. <span class="prov prov-doc">documented</span> The
    exception is a hidden hint zone marking a Climb, Ford or Shortcut, since all
    three use the same prop and would otherwise look identical. Their icons are
    `exMountainAccess30`/`40`, `exRiverFord30`/`40` and `exShortWay30`/`40`.

## Every property type, and where it is covered

Saber lists these as the props for ordinary zones in Expeditions.
<span class="prov prov-doc">documented</span>

| Property | What it makes the zone | Covered on |
|---|---|---|
| `ZonePropertyDeploy` | a place trucks arrive at the start of an expedition | [Deploy zones and FOBs](deploy-zones.html) |
| `ZonePropertyRecovery` | a target for truck recovery. Deploy zones only | [Deploy zones and FOBs](deploy-zones.html#recovery) |
| `ZonePropertyBaseBuilding` | the interaction zone of a buildable FOB module | [Deploy zones and FOBs](deploy-zones.html#every-module-is-two-zones) |
| `ZonePropertyInventoryStorage` | a store of items, fuel, parts and wheels: air drops, loot, the Base module | [Loot, storage and airdrops](storage-zones.html) |
| `ZonePropertyObjectConstructionInZone` | a delivery point that builds something, with no objective | [Construction zones](construction-zones.html) |
| `ZonePropertyHiddenHint` | a marker for a Climb, Ford or Shortcut, seen by binoculars, drone and on the map | this page, above |
| `ZonePropertyNotification` | a message shown when the player arrives, once (`executedOnce`) or every time. Invisible in game | not yet covered. Its message uses the same settings as objective notifications, see [Stages and substages](../50-missions/stages.html) |
| `ZonePropertyMinigame` | a place to play a minigame | [The assignment types](../50-missions/assignment-types.html#minigameinfo) |
| `ZonePropertyUpgradesGiver` | gives the player listed truck upgrades | not yet covered |
| `ZonePropertyGateway` | a link to another map | not usable yet, see below |

Deploy, Base Building, Inventory Storage, Object Construction and Hidden Hint props
each carry a `zoneDiscoverability` block, which decides whether the player can see
the zone before finding it. See [Hiding and revealing zones](discoverability.html).
The Notification prop has one too, but Saber says not to use it there, since that
zone is never shown in game.

!!! warning "Gateways do not work in Expeditions yet"
    Saber's guide says custom regions of several linked maps are not supported in
    Expeditions; only standalone maps are. <span class="prov prov-doc">documented</span>

### Props you should not add by hand

Some prop types exist but are not for you to pick.

- **Internal technical props**: `ZonePropertyFakeVisitZone`,
  `ZonePropertyInventoryStorageQuest`, `ZonePopertyObjectConstruction` (Saber's
  spelling) and `ZonePropertyScouting`. The game assigns these itself when you
  configure the matching objective. <span class="prov prov-doc">documented</span>
- **FOB module props**: `ZonePropertyFobModuleStorage`, `ZonePropertyWorkshop`,
  `ZonePropertyServiceStation`, `ZonePropertyParking`, `ZonePropertyDroneDelivery`,
  `ZonePropertySupplyShop`, `ZonePropertyTowTruck` and the others. These belong
  inside a **custom FOB module's** descriptor, never on a zone you place on a map.

!!! danger "FOB module props on a map zone can crash the game"
    Saber's guide is explicit: these props must be used only for configuring custom
    FOB modules, and assigning them to ordinary standalone zones "might cause a
    crash". <span class="prov prov-doc">documented</span> To give a map a workshop or
    a service station, give the player a place to **build** the module, as described
    on [Deploy zones and FOBs](deploy-zones.html). To make a new kind of module, see
    [Module descriptor reference](../60-custom/base-modules-reference.html).

## Checking your work

The packer validates some zone settings. Its errors are written to:

```
C:\Users\<username>\Documents\My Games\Expeditions\base\logs\ModMapError.txt
```

The editor will let you save a zone with wrong props, so read that log after a pack
that misbehaves. <span class="prov prov-doc">documented</span>

Also confirm your props survived the pack at all. Packing can regenerate the zone
list with empty settings; see
[Where everything lives](../00-start/where-things-live.html#packing-rewrites-some-of-your-work).
