---
title: Objectives in one page
part: Missions
order: 510
summary: The three kinds of objective, how they differ, and the single idea that the rest of the mission system is built on.
---

An **objective** is a job you give the player. There are three kinds, they all
live in the same file, and they share nearly every field.

## The three kinds

| Kind | The player starts it by | Use it for |
|---|---|---|
| **Expedition** | picking it on the Expedition Selection screen before deploying | the headline job. The reason to come to this map |
| **Contract** | accepting it in the world, during an expedition | optional side work |
| **Task** | driving to a specific zone that offers it | small local jobs, found by exploring |

An expedition and a contract are **the same record** with one number changed.
`contractType` is `1` for an expedition and `0` for a contract, and everything else
about them is identical. If a job turns out to be too small to headline a map, you
demote it by editing one digit.

A task is slightly different: it lives in its own list and it needs a **task giver
zone**, a place the player has to reach before the job is offered at all. Without
one, the task exists but can never be started.

There is no limit on how many of any kind a map can have.

!!! warning "Names must be unique across all three"
    A task and a contract with the same name cause undefined behaviour. Not an
    error message. Undefined behaviour. This is easy to do by accident when you
    duplicate something, and hard to spot afterwards.

## The one required objective

A map is only loadable if it has at least one **expedition**, plus at least one
deploy zone. <span class="prov prov-doc">documented</span>

And that expedition is allowed to be a Free Roam one, which is the cheapest thing
in the whole system: a single stage containing a single field. So the minimum map
is "drive around", and [that is what you should build
first](../00-start/map-that-loads.html).

Offering Free Roam is also just good practice even on a finished map. Some players
want to explore your terrain without a job attached, and it costs you one record.

## The idea everything else rests on: stages

Every objective, of all three kinds, is a list of **stages**.

- **Stages happen in order.** Stage 1 does not start until stage 0 is done.
- Inside a single stage you can put several assignments. Those happen in **any
  order**, and all of them must finish before the stage closes.

That is the whole of mission structure. There is no scripting language, no trigger
system and no conditions. You sequence a mission purely by choosing which stage
each assignment goes in.

Two jobs in one stage means *"do these in any order"*. The same two jobs in
consecutive stages means *"do this one, then that one"*.

[Stages and substages](stages.html) covers this properly, and it is the page to
read next.

## How many steps can one expedition have?

**As many as you like.** There is no limit in the file format.
<span class="prov prov-schema">schema only</span> The real ceiling is the player's
patience.

You can also make a mission wider instead of longer. Most assignment types accept
a **list** of targets, so a single step can mean "visit all six of these, in any
order" without adding any stages at all.

## Where it is all stored

One file, `objective_settings.json`, with four sections:

| Section | Holds |
|---|---|
| `contractsSettings` | expeditions **and** contracts, told apart by `contractType` |
| `tasksSettings` | tasks |
| `employer` | custom employers, if you make one |
| `name` | the map |

You edit it through the zone settings tool, or by hand, since it is plain JSON.

## What to read next

<ul class="cards">
<li><a href="stages.html"><strong>Stages and substages</strong><span>How to order a mission. The core mechanic.</span></a></li>
<li><a href="assignment-types.html"><strong>The assignment types</strong><span>Every kind of thing you can ask a player to do.</span></a></li>
<li><a href="rewards.html"><strong>Rewards</strong><span>Money, trucks, specialists, bases, and your own custom content.</span></a></li>
<li><a href="building-a-story.html"><strong>Building a story</strong><span>Making the world change as the player progresses.</span></a></li>
</ul>
