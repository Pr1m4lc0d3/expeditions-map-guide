---
title: The objective system map
part: Missions
order: 505
summary: Every kind of objective, stage, lock and reward in one place, with how far each has been proven, for planning a story.
status: draft
---

This page lists everything a story can be built from, and how sure we are that it works
on a custom map. Each part has its own page in this section with the detail.

!!! warning "This page is a draft"
    Much of it is still untested on custom maps. The status column tells you what has
    actually been run.

| Status | Means |
|---|---|
| PROVEN | run in game on a custom map |
| ON A CUSTOM MAP | written into a custom map, but not re-tested for this page |
| DOCUMENTED | Saber's Expeditions guide describes it; not tried on a custom map |
| ENGINE ONLY | in the engine's schema but missing from Saber's guide; unknown if mods can use it |

## 1. The shape of a story

```
Region (optional)
  Map
    Objective            Expedition | Contract | Task
      Lock               blockerObjectives, requirements
      Stage [0]          stages run in order
        Substage         substages in one stage run in any order
        Stage reward     fires when this stage closes
      Stage [1] ...
      Final rewards      fire when the objective finishes
```

Three ideas carry every story:

- **Order** comes from stages. Same stage means any order; next stage means after.
- **Gating** comes from locks. One objective opens another.
- **Change** comes from rewards. A reward can change the world mid-story.

## 2. Kinds of objective

| Kind | Where it lives | How the player starts it | Status |
|---|---|---|---|
| Expedition | `contractsSettings`, `contractType` 1 | Expedition selection menu | PROVEN |
| Free Roam | an Expedition with one stage holding only `freeRoamInfo` | Menu | PROVEN |
| Contract | `contractsSettings`, `contractType` 0 | On the map | ON A CUSTOM MAP |
| Task | `tasksSettings`, needs `taskGiverZone` | Driving to a giver zone | ON A CUSTOM MAP |
| Contest | `contestSettings` | Not used in Expeditions, says Saber | none |
| Regional contract | region file, zones from all maps | Described for SnowRunner only | Not needed: see below |

A normal Expedition stored on one map already spans maps, so a separate regional
contract hasn't been needed. PROVEN 11-05.

Every map needs one Expedition and one deploy zone. Give every map a Free Roam too.
Objective names must be unique across all kinds.

## 3. Things a stage can ask for

### Documented substages

| Section | Player does | Key fields | Status |
|---|---|---|---|
| `visitAllZones` | Reach zones | `zones[].globalZoneId`, `uiDesc` | PROVEN, also across maps |
| `freeRoamInfo` | Nothing: Free Roam only | `map`, `uiDesc` | PROVEN |
| `takeInventory` | Collect items from zones | `zoneToTakeInvFrom[].zoneGlobalId`, `inventoryToTake` | ON A CUSTOM MAP |
| `objectConstruction` | Deliver items, fuel, repairs, power; can build a model | `zoneToFill[].globalZoneId`, `inventory`, `fuelNum`, `repairsNum`, `electroNum`, `model` | ON A CUSTOM MAP |
| `truckDelivery` | Drive a placed truck to a zone | `globalZoneDeliveryId`, `afterStageFinished` | ON A CUSTOM MAP |
| `scoutingInfo` | Explore an area to a percentage | `scoutingsProp[]`: `zoneGlobalId`, `radius`, `winCondition`, offset | DOCUMENTED |
| `minigameInfo` | Play minigames | `minigames[]`: `zoneGlobalId`, `name`; settings sit on the zone | DOCUMENTED |
| `makeActionInZone` | Seismic prospecting at hidden zones | Same shape as `visitAllZones` | DOCUMENTED |

### In the engine, missing from Saber's guide

| Section | Looks like | Zone prop | Status |
|---|---|---|---|
| `objectInteraction` | Interact with a placed, animated model | `interactionZoneId`, `modelPlacementZoneId`, `animModelName`, `animStagesProgress` | ENGINE ONLY |
| `puzzleInfo` | A puzzle at a zone | `ZonePropertyPuzzleZone`; 2 in the vanilla dump | ENGINE ONLY |
| `cutsceneInfo` | Play a cutscene | `ZonePropertyCutscene`; 29 in the vanilla dump | ENGINE ONLY |
| `otherMapGatewaySelectionSettings` | Unknown, tied to gateways | Hidden from mods | ENGINE ONLY |
| `tutorialViewsOnCompleteStage` | Shows a tutorial when a stage ends | None | ENGINE ONLY |

### Minigames

Settings go on a `ZonePropertyMinigame` zone. The count is how many sit in the vanilla game dump.

| Type | Saber's page | Vanilla count | Status |
|---|---|---|---|
| `CAMERA` | Taking photos | 195 | DOCUMENTED |
| `VISUAL_INSPECTION` | Visual inspection | 118 | DOCUMENTED |
| `PROCESS_POINTS` | Probably scanning with a drone (unconfirmed) | 52 | DOCUMENTED |
| `ECHOLOT_SCAN` | Echo sounder | 44 | DOCUMENTED |
| `LOOK_AT_OBJECT` | None found | Not counted | ENGINE ONLY |

## 4. Locks and requirements

| Field | Effect | Status |
|---|---|---|
| `blockerObjectives` | Locks until listed objectives finish. Use the full saved name `mod_<id>_<name>`. Hidden in the editor; see [Gateways between maps](../40-zones/gateways.html) | PROVEN |
| `blockerMap` | Saber: locks until a map is opened. Did not lock a menu row | Failed in test |
| `zoneDiscoverability` | Hides a zone until found by truck, drone or binoculars | PROVEN on a deploy zone |
| `requiredInventory` | Items needed | DOCUMENTED |
| `requiredSpecialities` | Specialists needed | DOCUMENTED |
| `requiredTruckAddons` | Truck addons needed | DOCUMENTED |

## 5. Rewards

Rewards go on the whole objective, or on one stage to fire mid-story.

| Reward | Gives | Status |
|---|---|---|
| `ObjectiveRewardMoney` | Money | PROVEN |
| `ObjectiveRewardOpenZoneProperties` | Opens a zone with new props, such as a base | PROVEN |
| `ObjectiveRewardUpdateZoneProperties` | Adds props to a zone; `zoneSettingsToRemove` takes them off | DOCUMENTED |
| `ObjectiveRewardUnlock` | Unlocks a truck or upgrade | DOCUMENTED |
| `ObjectiveRewardItem` | Gives a truck or upgrade | DOCUMENTED |
| `ObjectiveRewardBaseUpgrade` | Unlocks an FOB module | DOCUMENTED |
| `ObjectiveRewardSpecialist` | Unlocks a specialist | DOCUMENTED |
| `ObjectiveRewardSticker` | Gives a sticker | DOCUMENTED |
| `ObjectiveRewardAddItemsToZone` | Puts items in a zone | ENGINE ONLY |
| `ObjectiveRewardOverlayState` | Changes an overlay's state | ENGINE ONLY |
| `ObjectiveRewardZoneInventoryRandModifier` | Changes a zone's random loot | ENGINE ONLY |
| `ContestResultRewards` | Nothing: it has never paid out on our maps | Do not use |
| `ObjectiveRewardsUpgradeGarage` | Not used in Expeditions | Do not use |

**Bonus rewards**, Expeditions only: extra money for how the player did it. Conditions
include little damage, no recovery, few engine stalls, not using an item, and few
minigame failures. DOCUMENTED.

## 6. Presentation

| Field | Effect | Status |
|---|---|---|
| `description`, `uiDesc` | Listing and objective text, plain text only | PROVEN |
| `employer` | Name and logo | PROVEN |
| `notification` on a zone | Message when reached | PROVEN |
| `zoneDiscoverability.discoveryMessage` | Message when found | PROVEN |
| `difficulty`, `wayLength`, `tips` | Details; not shown on the selection screen we tested | Unknown |
| `prepayment` | Money up front | ON A CUSTOM MAP |
| `radiusSett` | Shows a search area, not the exact zone | ON A CUSTOM MAP |
| Fake zones | Wrong spots with their own message | ON A CUSTOM MAP |
| `uiMinimapScreenshot` | Nothing: No Signal stays | Failed in test |
| `UI_` keys with `texts\strings_english.str` | Showed the raw key on a map | Failed in test |

Zones that tell a story without an objective: `ZonePropertyNotification`,
`ZonePropertyHiddenHint`, `ZonePropertyWatchpoint`. DOCUMENTED or ENGINE ONLY; not tried.

## 7. Traps

1. A lock needs the full saved name. A plain name never clears.
2. Start the chain from the region group, or its saved name differs.
3. The pack rewrites references to another map as `level_<name>`. Correct them to `mod_level_<name>` in the `.pak` after every pack.
4. Every stage needs one required substage.
5. A dangling zone reference hangs the Deploy screen.
6. A null `localOffsetScoutingAreaRelativeZone` crashes.
7. Opening a module zone before its base exists breaks every popup after it.
8. Finishing an Expedition keeps the player on the map.
9. Hidden editor fields survive a pack, so they can be written in the JSON.
10. Schema enum listings repeat the first value, so a saved number is the listed index
    minus one: `contractType` 1 is EXPEDITION.

## 8. Story patterns

| Pattern | Built from | Status |
|---|---|---|
| Unlock a map | Expedition, then `blockerObjectives` on its Free Roam | PROVEN |
| Journey across maps | One Expedition with stages on each map | PROVEN |
| Earn a base | Stage or final reward with `ObjectiveRewardOpenZoneProperties` | PROVEN |
| Hidden camp | Deploy zone starting `NOT_EXPLORED` | PROVEN |
| Clear a blockage | `objectConstruction`, then `zoneSettingsToRemove` | Documented parts |
| Rebuild something | `objectConstruction` with Model Building Settings | ON A CUSTOM MAP |
| Find the site | `radiusSett` plus fake zones | ON A CUSTOM MAP |
| Survey an area | `scoutingInfo`, then a reward | DOCUMENTED |
| Investigate | `minigameInfo`: photos, inspection | DOCUMENTED |
| Rescue | `truckDelivery` with a placed truck | ON A CUSTOM MAP |
| Side jobs | Tasks at giver zones | ON A CUSTOM MAP |
| Earn a specialist | `ObjectiveRewardSpecialist` | DOCUMENTED |
