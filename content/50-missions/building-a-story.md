---
title: Building a story
part: Missions
order: 550
summary: How to make the map change as the player progresses, which is what progression actually feels like from inside the game.
---

You have stages, and stages have rewards. Put those two together and you have
progression, because **a reward can change the map**.

That is the whole technique, and it is better than it sounds.

## The obvious approach, and why it is not available

The natural way to build a campaign is to lock mission B until mission A is done.
There is a field for exactly that, `blockerObjectives`, which takes a list of
objective names.

The official guide says the field is "currently absent".

Here is the more precise situation. The field exists on every objective, and the
editor's own type schema marks it **hidden from mod tools** rather than absent.
<span class="prov prov-schema">schema only</span> It sits in every custom map's file
as an empty list. So writing it in by hand may well work.

!!! warning "Worth an experiment, not a foundation"
    Nobody has confirmed that `blockerObjectives` functions in a custom map. If you
    test it, you will have learned something genuinely new. Until then, do not build
    a multi-mission campaign that depends on it.

## What actually works: rewards that reshape the world

Three reward types change zones, and any stage can carry them:

| Reward | Effect |
|---|---|
| `ObjectiveRewardOpenZoneProperties` | a zone the player could not use becomes usable, with properties you supply |
| `ObjectiveRewardUpdateZoneProperties` | an existing zone gains properties |
| `zoneSettingsToRemove` | an existing zone loses properties |

So a mission can open up territory, upgrade a place the player already knows, or
clear an obstacle, all as the consequence of finishing a step.

## A worked example

Here is a three-stage expedition where every stage visibly changes the map.

```
stage[0]   Reach the ridge
           reward → OpenZoneProperties
                    "Rattlesnake Outpost" becomes a deploy zone

stage[1]   Deliver fuel to the outpost
           reward → UpdateZoneProperties
                    the outpost gains a supply shop

stage[2]   Clear the cave blockage
           reward → UpdateZoneProperties + zoneSettingsToRemove
                    the blockage stops being an obstacle
```

Play that through and it does not feel like a checklist. It feels like establishing
a foothold: you find the place, you supply it, it becomes useful, and then you open
the route beyond it. The player's map genuinely changes shape as they work.

None of that needed a script.

## Three things that will trip you up

**The zone has to exist already.** `OpenZoneProperties` *reveals* a zone. It does not
create one. You still place the zone object in the map editor first, exactly as you
would for any other zone, and the reward attaches properties to it later. If the
locator is not there, nothing appears.

**Zone names in reward blocks are written differently.** Everywhere else in the
objective file, a zone is referred to with the map token, then `||`, then the name.
Inside these reward blocks it is the **short name only**, with the map supplied
separately in a `mapId` field. Mixing the two forms up is a common and silent
mistake.

**Removing properties is not the same as deleting the zone.** The zone stays. It just
stops doing the thing you removed. That is usually what you want, because the player
has seen that place and it should not vanish.

## Progress carries between expeditions

Two expeditions on the same map are not independent, which you can use
deliberately. <span class="prov prov-doc">documented</span>

**Persists between expeditions on one map:**

- ground the player has explored
- FOB modules they have built
- zones that have been opened

**Resets:**

- air drop locations and contents are randomised again
- FOB module stock, fuel and supplies refresh

**The one exception:** items the player put in the Warehouse, the `EXTRA_STORAGE`
module, are still there next time.

So you can write a second expedition that assumes the first one's base exists. A
player who does them out of order gets a slightly different experience rather than a
broken one, since expeditions can be played in any order when nothing locks them.

## Telling the story in words

The mechanics above carry the shape of a story. The text carries the rest, and there
are more places to put it than people use:

- `uiDesc` and `description` on the objective, which is the briefing
- `uiDesc` on every single assignment, which is the current instruction
- a `notification` on each individual target, which fires when the player gets there

That last one is the most underused thing in the system. A short line of text when
the player arrives somewhere costs nothing and does more for atmosphere than another
objective. It is also the only notification that reliably fires on
`objectConstruction` and `visitAllZones`, so put your writing there rather than at
the assignment level.

`rewardDescription` is worth filling in too, since an unexplained reward panel reads
as an oversight.

## A design note on hiding things

Every assignment target can carry a `radiusSett`, which swaps the exact marker for a
search circle. It is one setting and it changes the whole character of a job.

A marker says *go here*. A circle says *it is somewhere in there*. For a map about
expedition and exploration, the circle is almost always the better choice, and a mission
built entirely from precise waypoints will feel like a delivery route no matter how
good the terrain is.
