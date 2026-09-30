---
title: Rewards
part: Missions
order: 540
summary: Money, trucks, specialists, FOB modules and your own custom content. Plus the reward classes that look fine and never pay.
---

## Two places to attach a reward

- on the **objective**, paid when the whole thing is finished
- on each **stage**, paid the moment that stage closes

Both draw from the same list of reward types. Stage rewards are the more
interesting of the two, because they can change the map while the player is still
on it. See [building a story](building-a-story.html).

## What you can give

| Reward | Gives the player | |
|---|---|---|
| `ObjectiveRewardMoney` | cash | <span class="prov prov-doc">documented</span> |
| `ObjectiveRewardUnlock` | a truck or upgrade becomes purchasable | <span class="prov prov-doc">documented</span> |
| `ObjectiveRewardItem` | a truck or upgrade, handed over outright | <span class="prov prov-doc">documented</span> |
| `ObjectiveRewardSticker` | a truck sticker | <span class="prov prov-doc">documented</span> |
| `ObjectiveRewardSpecialist` | a crew member becomes available | <span class="prov prov-doc">documented</span> |
| `ObjectiveRewardBaseUpgrade` | a FOB module is unlocked | <span class="prov prov-doc">documented</span> |
| `ObjectiveRewardOpenZoneProperties` | **a new zone appears**, with properties you define | <span class="prov prov-doc">documented</span> |
| `ObjectiveRewardUpdateZoneProperties` | **an existing zone changes**, gaining or losing properties | <span class="prov prov-doc">documented</span> |
| `ObjectiveRewardOpenZoneDesc` | the map text and icons for a newly revealed zone | <span class="prov prov-schema">schema only</span> |
| `ObjectiveRewardExperience` | experience | <span class="prov prov-schema">schema only</span> |
| `ObjectiveRewardOverlayState` | changes an overlay's state, such as a road surface or a bridge deck | <span class="prov prov-schema">schema only</span> |
| `ObjectiveRewardZoneInventoryRandModifier` | alters what a zone randomly spawns | <span class="prov prov-schema">schema only</span> |
| `ObjectiveRewardsByTime` | rewards gated on elapsed time | <span class="prov prov-schema">schema only</span> |

The last five are absent from the official guides entirely. `ObjectiveRewardOverlayState`
is the most immediately useful of them, because it means the visible state of a road
or bridge can change as a reward.

!!! danger "Rewards that never pay"
    Several reward types are technical scaffolding or are marked for removal. They
    are accepted, they look correct in the file, and they do nothing:

    `ContestResultRewards`, `ObjectiveRewardAddItemsToZone`,
    `ObjectiveRewardsUpgradeGarage`, `ObjectiveSingleRewardUnlockOnce`,
    `ObjectiveRewardSettingsBase`, `ObjectiveRewardListener`,
    `ObjectiveRewardTrialPartItem`

    `ContestResultRewards` is the one that bites, because it takes an `amount` and
    a `timeLimit` and therefore looks exactly like a working money reward. If it is
    an objective's only reward, that objective pays **nothing**.

## Rewarding your own custom content

Short answer: yes, for all three of the things people usually want.

### Your own devices and items

**Works.** A custom inventory item has an id, and the objective system takes custom
ids the same way it takes built-in ones. You can require them, ask the player to
collect them, and hand them over as rewards with `ObjectiveRewardItem`.

!!! warning "One requirement that will stop your expedition dead"
    If a custom item appears in an expedition's `requiredInventory`, that item
    **must** have `canTakeInHq` enabled. <span class="prov prov-doc">documented</span>

    Without it the player cannot load the item at Headquarters, so they can never
    satisfy the requirement, so they can never start the expedition. The expedition
    simply refuses, and nothing explains why.

### Your own bases

**Works.** `ObjectiveRewardBaseUpgrade` takes a FOB module id, and custom FOB
modules are a supported, documented entity. The built-in ids are:

```
BASE_MODULE     SUPPLY_SHOP    WORKSHOP       SERVICE_STATION   GAS_STATION
REPAIR_ZONE     PARKING        GENERATOR      ANTENNA           HELICOPTER
DRONE_BASE      TOW_TRUCK      EXTRA_STORAGE  DOUBLE_STOCK      NOTE
```

This is a good reward for a mid-mission stage. "Get the generator running" that
actually unlocks the generator module reads as real progress.

### Your own specialists

**Works for the built-in crew. Probably works for yours.**
<span class="prov prov-unver">unverified</span>

`ObjectiveRewardSpecialist` takes an id, and the documented examples are built-in
crew like `Mechanic_01`, `Jaeger_02` and `Hydrologist_03`.

Custom specialist descriptors do carry an `isLocked` flag, which is exactly the
mechanism such a reward would open, and it defaults to unlocked so a custom crew
member is normally available from the start anyway.

What is **not** established is the id string a custom specialist answers to. The
descriptor file contains no id field at all, and identity appears to come from the
pak's own name. So this is likely to work and the exact spelling is a guess. Test it
before you build a mission whose payoff is a custom crew member.

## Bonus rewards

Extra money for playing well, rather than for finishing. **Expeditions only**, not
contracts or tasks.

Each one carries a description and an amount, and most carry a limit. The engine has
**twenty** conditions. The official guides cover twelve.

| Documented | Undocumented <span class="prov prov-schema">schema only</span> |
|---|---|
| `BonusConditionDamageTaken` | `BonusConditionCompleteExpedition` |
| `BonusConditionNoRecovery` | `BonusConditionDriveLessThenLimit` |
| `BonusConditionEngineStall` | `BonusConditionSpendFuelLessThenLimit` |
| `BonusConditionTireInflation` | `BonusConditionSpendFuelMoreThanLimitInOneGo` |
| `BonusConditionItemConsumed` | `BonusConditionFinishExpWithEmptyInventory` |
| `BonusConditionDoNotUseItem` | `BonusConditionFinishExpOnSpecificTruckType` |
| `BonusConditionDetectResource` | `BonusConditionDontSkipTime` |
| `BonusConditionMinigameTryLimit` | `BonusConditionHaveMoreItemsThanLimit` |
| | `BonusConditionDriveXMetersOnLowTiresInOneGo` |
| | `BonusConditionCollectMoreItemsThenLimitOnExp` |

Several of the undocumented ones are more interesting than the documented ones.
"Finish with an empty inventory", "finish on a specific truck type" and "do not skip
time" are all real design levers. At least one undocumented condition is already in
use by a published custom map, so the group is not dead code.

`BonusConditionEngineStall` deserves a note: it counts engine stalls for a given
reason, and the base game mostly uses it with `ROLL_OVER`. So the natural reading of
it is "do not roll your truck".

## Gating an expedition before it starts

Three lists decide whether a player may begin an expedition at all. All three are
**expeditions only**.

| List | Requires |
|---|---|
| `requiredInventory` | items, by type or id, in the stated quantity |
| `requiredSpecialities` | specific crew |
| `requiredTruckAddons` | `SEISMIC_VIBRATOR`, `METAL_DETECTOR` or `SIDEBOARD` |

These are good for making a mission feel prepared for rather than stumbled into.
Use them sparingly, because a requirement the player cannot work out how to satisfy
just looks like a broken map.
