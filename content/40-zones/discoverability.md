---
title: Hiding and revealing zones
part: Zones
order: 450
status: draft
summary: Fog of war, and the setting that will accidentally hide a zone you wanted available.
---

Most zone props carry a `zoneDiscoverability` block. It decides whether the player
can see the zone when the expedition starts, and if not, how they get to find it: by
driving there, by flying a drone over it, or by spotting it through binoculars.

Used on purpose it is one of the best tools a map has, because finding things is the
point of an expedition. Used by accident, it hides a zone you meant to be open and
gives you no hint why.

!!! note "What on this page has been tested"
    That a zone with **no** discoverability block is simply available is proven:
    deploy zones set up that way on working maps load and deploy. The rest is from
    Saber's guides and from the settings in working maps. It has not been tested
    state by state in game, and the specialist requirements and discovery rewards
    are untested.

## Leave it empty unless you mean it

**A zone with no discoverability settings is simply available.** Its marker is
there from the start, and nothing has to be found. This is the right answer far more
often than people expect: a deploy zone, a store, a delivery target the briefing
already tells the player about.

In Zone Settings an unused block is `null`. On the working maps this guide was built
from, every main deploy zone has it `null`.

## The states

`state` is where the zone stands at the moment it spawns.
<span class="prov prov-doc">documented</span>

| State | What the player sees |
|---|---|
| `NOT_EXPLORED` | nothing. The zone is not on the map |
| `SEEN_BY_OPTCS_QUESTION_MARK` | a question mark on the map. Partly discovered |
| `SEEN_BY_OPTCS_DISCOVERED` | the full marker, as if found with binoculars |
| `EXPLORED_BY_DRONE_FLIGHT_IN` | the full marker, as if found by drone |
| `EXPLORED_BY_TRUCK` | the full marker, as if found by truck |

`SEEN_BY_OPTCS` is Saber's spelling, and the one the game uses.

## The trap: copying a block

The block is easy to copy from another zone, and that is where the trouble starts.
On the working maps examined, **every** zone that has a discoverability block at all
has the same state value, `0`, and it belongs to zones the player is meant to find.
That value is the first in the list, which reads as `NOT_EXPLORED`.
<span class="prov prov-unver">unverified</span> that `0` is `NOT_EXPLORED`.

So copying a block from a typical existing zone onto one you want open usually
copies "not explored", and **hides** it. The zone works perfectly and the player
never sees it.

If a zone you expected on the map is missing, look at its `zoneDiscoverability`
before anything else. Delete the block if the zone should simply be available.

!!! warning "Do not strip discovery from someone else's design"
    The reverse is also a mistake. A secondary deploy zone left `NOT_EXPLORED` is one
    of Saber's two documented ways to open an outpost later, and it is meant to be
    found. <span class="prov prov-doc">documented</span> Removing the block to "fix"
    a missing outpost destroys that design.

## How a zone can be found

Three switches say which methods can discover the zone:

| Field | Discovered by |
|---|---|
| `discoverableByTruck` | driving to it |
| `discoverableByDrone` | the drone |
| `discoverableByBinocular` | binoculars |

<span class="prov prov-doc">documented</span> Turn off the ones you do not want.
A zone the player must physically reach, for example, would keep only the truck.

### Requiring a specialist

Two more fields require a particular kind of specialist for a method to work:

| Field | Meaning |
|---|---|
| `requiredSpecialistDrone` | the specialist type needed to discover this zone by drone |
| `requiredSpecialistBinocular` | the specialist type needed to discover it with binoculars |

The value **`NONE`** switches the requirement off. <span class="prov prov-doc">documented</span>

In the saved file these are stored as numbers, not names. Which number is which
specialist type is not documented, and has not been worked out here. Choose the
value in the Zone Settings plugin, which shows the names, rather than typing a number.
<span class="prov prov-unver">unverified</span> how either requirement behaves in game.

## Messages and rewards for finding it

| Field | What it does |
|---|---|
| `discoveryMessage` | text shown when the player discovers the zone |
| `discoveryRewardMoney` | a reward paid on discovery |

`discoveryRewardMoney` offers two reward classes. Use `ObjectiveRewardMoney`. Saber
says the other, `ContestResultRewards`, should not be used here, and elsewhere in
Expeditions it never pays out. <span class="prov prov-doc">documented</span>
<span class="prov prov-unver">unverified</span> in game.

## Other ways a zone becomes visible

Discoverability is not the only thing that reveals a zone.

- **Deploying.** Trucks arriving at a deploy zone uncover the ground around it:
  `fogOfWarUnlockRadius` fully, `fogOfWarUnlockRadiusTransparent` partly. See
  [Deploy zones and FOBs](deploy-zones.html).
- **Rewards.** `ObjectiveRewardOpenZoneProperties` opens a zone with new props as an
  objective reward. The locator has to be on the map already; the reward reveals it,
  it does not create it. See [Building a story](../50-missions/building-a-story.html).
- **Exploration persists.** Ground the player has explored stays explored in later
  expeditions on the same map. <span class="prov prov-doc">documented</span>

## Scouting objectives

A `scoutingInfo` assignment asks the player to explore an area around a target
zone. In current versions that target zone hides itself automatically; older guides
said to add a `ZonePropertyHiddenHint` with discovery switched off, and that is no
longer needed. <span class="prov prov-doc">documented</span>

The catch Saber points out: do not use the same zone in another objective that could
make it visible, or the hidden centre of the search area appears on the map. Give a
scouting target its own zone. The assignment itself is covered on
[The assignment types](../50-missions/assignment-types.html#scoutinginfo).

To show the player a search circle rather than an exact marker on any assignment, use
`radiusSett` on the target. See
[Stages and substages](../50-missions/stages.html#hiding-the-target).

## What is not known yet

- which stored number corresponds to which state and which specialist type
- whether each state behaves exactly as Saber describes in a running game
- how the specialist requirements behave in game
- whether `discoveryRewardMoney` pays out
