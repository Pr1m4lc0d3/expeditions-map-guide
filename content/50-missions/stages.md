---
title: Stages and substages
part: Missions
order: 520
summary: How you order a mission. Stages run in sequence, the assignments inside one stage run in any order, and that is the whole mechanic.
---

This is the one concept the official guides bury, and once you have it the rest of
the mission system is just filling in fields.

## Two rules

An objective is a list of **stages**. Each stage contains one or more
**assignments**, which the software calls *substages*.

- **Stages run in order.** Stage 0, then stage 1, then stage 2.
- **Assignments inside one stage run in any order**, and all must finish before
  that stage closes.

That is it. There is no scripting, no triggers, no conditions, no branching.

## What that looks like

Say you want the player to reach a ridge, grab a winch anchor, then bridge a wash,
then tow a wreck home. You do not want to force an order on the first two, but the
bridge must come after both and the tow must come last.

```
Expedition "Escape the Canyon"

  stage[0]     ├─ visitAllZones       "Reach the ridge"
               └─ takeInventory       "Grab the winch anchor"
                    ↑ either order, both required

  stage[1]     └─ objectConstruction  "Bridge the wash"
                    ↑ locked until stage 0 is fully done

  stage[2]     └─ truckDelivery       "Tow the wreck home"
                    ↑ locked until stage 1 is fully done
```

Three stages, four assignments. The ordering you wanted came entirely from
choosing which stage each assignment went into.

If you had put the bridge in stage 0 as well, the player could have bridged the
wash before ever reaching the ridge. If you had split the ridge and the anchor into
stages 0 and 1, you would have forced an order you did not want.

**That decision is mission design.** There is nothing else to it.

## Making a step optional

Any assignment can be marked `OptionalToPerform`, which lets the player skip it.

The usual reason is to avoid stranding someone. Suppose stage 1 asks the player to
install a camera trap, which needs a camera trap in their inventory. You add a
`takeInventory` step so they can go and find one. But a player who already brought
one should not have to.

So make the "go and find one" step optional, and put it in **the same stage** as
the install step:

```
  stage[0]     ├─ takeInventory       "Collect a camera trap"   (optional)
               └─ objectConstruction  "Install the camera trap" (required)
```

!!! danger "A stage where every assignment is optional is an error"
    Every stage must contain at least one **required** assignment. A stage made
    entirely of optional steps is invalid and will error.
    <span class="prov prov-doc">documented</span>

    This catches people out because it looks reasonable. If you give that optional
    `takeInventory` a stage of its own, the stage has nothing required in it and
    the objective breaks. Pair it with the required step instead, as above.

## The notification trap

Most assignments can show the player a message when they are completed, and there
are two places to put one:

- on the **whole assignment**
- on each **individual target** inside it

For `objectConstruction` and `visitAllZones`, the whole-assignment notification
**does not fire**. <span class="prov prov-doc">documented</span> Only the per-target
one works. If your message never appears, this is why: move it down a level.

## One assignment, several targets

You do not always need more stages. Most assignment types take a **list** of
targets, and the player must complete all of them in any order.

So "visit all six lookouts" is one assignment with six entries, not six stages. The
types that accept multiple targets are `objectConstruction`, `takeInventory`,
`truckDelivery`, `visitAllZones`, `minigameInfo`, `scoutingInfo` and the
seismograph.

Use extra stages when **order matters**. Use extra targets when it does not.

## Hiding the target

By default the player is shown exactly where to go. Often you would rather make
them look.

Each target can carry a `radiusSett`, which replaces the precise marker with a
circle of a given radius. The player gets an area to search instead of a waypoint.
This is what turns a fetch quest into exploration, and it is one setting.

## Rewards at the end of a stage

Each stage has its own rewards, paid the moment that stage closes rather than when
the whole objective finishes.

This is more powerful than it sounds, because rewards can change the map itself.
It is how you make the world open up as the player progresses, and it gets [its own
page](building-a-story.html).

## Things to check before you pack

- every stage has at least one required assignment
- every zone name you typed actually exists, spelled identically
- your notifications are on the target, not the assignment, for
  `objectConstruction` and `visitAllZones`
- order really does matter everywhere you used a separate stage
