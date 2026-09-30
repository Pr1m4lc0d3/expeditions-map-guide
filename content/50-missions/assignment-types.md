---
title: The assignment types
part: Missions
order: 530
summary: Every kind of job you can give a player, what each one needs, and the three that exist in the engine but not in the official guides.
---

An assignment is one thing you ask the player to do. A stage holds one or more of
them. There are **eleven** kinds, and the official guides document **eight**.

## The eight documented kinds

### visitAllZones

Reach one or more places. The simplest assignment and the one you will use most.

Each target can optionally be reached by **drone** instead of by truck, or by drone
**only**.

!!! warning "Drone-only needs two settings, not one"
    To require the drone you must turn on *both* `visitWithDroneOnly` **and**
    `mayVisitZoneWithDrone`. With only the first, trucks are forbidden and drones
    were never allowed, so the zone becomes unreachable by any means.
    <span class="prov prov-doc">documented</span>

    Also: the default drone cannot fly within **170 m** of the map edge, and cannot
    climb more than **30 m** above the truck. A drone-only target outside those
    limits is impossible. <span class="prov prov-doc">documented</span>

### takeInventory

Collect specific items from specific places. You name the item type, optionally a
specific item id, and how many.

Works with custom items. If you have made your own device, its id goes here like
any other.

### objectConstruction

Deliver something to a place. That something can be an inventory item, **fuel**,
**repair parts**, or any combination. At least one of the three must be set or
there is nothing to deliver.

The name comes from what it is usually used for: tying the delivery to a model that
appears once the goods arrive, which is how bridges get built. That part is
optional, and the delivery works fine without it.

Two useful extras:

- `additionalUnloadZones` lets the goods be delivered to an alternative place. The
  base game uses this for bridges buildable from either bank.
- `modelPlacementZones` blocks the delivery while a truck is parked somewhere it
  would be clipped by the model appearing.

### truckDelivery

Drive a truck that is already placed on the map to a destination. The truck needs
an **Id** in the editor, and the same string goes in the assignment.

!!! warning "Do not use REWARD to give the truck away"
    `afterStageFinished: REWARD` does nothing in Expeditions. It behaves as
    `DO_NOTHING`: the truck stays on the map, the player does not get it, and it
    never appears on the rewards screen. <span class="prov prov-doc">documented</span>

    Use `DESTROY`, which is what the base game does, and grant the vehicle properly
    through the [rewards list](rewards.html).

### scoutingInfo

Explore an area. You define it with a hidden zone at the centre, a radius, and the
percentage of the area that must be uncovered. A `winCondition` of `0.75` means 75%.

The centre can be offset from the zone if you want the search area somewhere the
zone object is not.

!!! danger "The one crash in the objective system"
    `localOffsetScoutingAreaRelativeZone` **must not be left empty.** Leaving it
    unset crashes the game. <span class="prov prov-doc">documented</span>

    If you want no offset, you still have to pick the `Vector2d` type and leave the
    x and y values at zero. An explicit zero is fine. Nothing is not.

The target zone hides itself automatically in current versions, so you do not need
to do anything extra to keep it off the map.

### minigameInfo

Play a minigame. Five kinds exist in the engine:

| Minigame | What the player does |
|---|---|
| Camera | photograph a subject at an expected focus, zoom and angle |
| Echolot | scan across zones with a limited number of charges |
| ProcessPoints | fly the drone to track a moving circle |
| LookAtObject | observe a particular object |
| VisualInspection | inspect marked points on an object |

### Seismograph

Trigger seismic readings at zones that are deliberately not shown on the map, so
the player has to find them.

### freeRoamInfo

Not really an assignment. It marks an expedition as the Free Roam one.

!!! tip "Free Roam has strict shape"
    A Free Roam expedition is **one stage containing only `freeRoamInfo`**. Nothing
    else in that stage, and no other stages.
    <span class="prov prov-doc">documented</span>

    Its `map` field holds the name of your own map's XML file. Pointing it at a
    *different* map is a real and confusing bug, and it is easy to inherit by
    copying someone else's map as a starting point.

## The three undocumented kinds

These are in the editor's type schema **and** referenced in the shipped game code,
so they are real features. They are simply missing from the official guides, and as
far as is known nobody has used them in a custom map.

| Field | Appears to be |
|---|---|
| `objectInteraction` | interact with a placed object |
| `makeActionInZone` | perform an action in a zone. It reuses the same settings type as `visitAllZones`, so it is shaped like a visit |
| `puzzleInfo` | a puzzle, with a starting zone and a list of puzzle properties |

<span class="prov prov-schema">schema only</span>

Treat these as worth an experiment, not as something to build a map around. If you
do get one working, that is genuinely new information for everyone.

There is also `cutsceneInfo`, which plays a cutscene rather than asking for
anything, and a gateway type the base game uses to move players between maps which
is deliberately hidden from mod tools.

## The field name the guides get wrong

Every assignment points at a zone, and the official guides call that field
`globalZoneId` throughout. The actual files do not agree:

| Assignment | The field is really called |
|---|---|
| `visitAllZones`, `objectConstruction` | `globalZoneId` |
| `takeInventory`, `scoutingInfo` | `zoneGlobalId` |
| `truckDelivery` | `globalZoneDeliveryId` |

If you are editing JSON by hand, or writing anything that reads these files, expect
all three spellings.

## The failure they all share

Whatever the assignment, a zone reference that points at a name which does not
exist will **hang the Deploy screen forever**. No popup, no error, no log entry.

It is the single most common way to lose an evening, and the fix is always the
same: check every zone name against the zones that actually exist, character for
character.
