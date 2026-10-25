---
title: Descriptor settings
part: Appendix B - specialists
order: 947
summary: "Every field of a specialist descriptor: type, engine default, what it does and the rule that applies."
---

# Descriptor settings

A specialist is one JSON file, `SpecialistDesc`, inside a pak named
`SpecialistDesc_<name>.pak`. These are all twelve fields the engine defines for
it, with the type and default from the editor's type definitions. How to
create and pack the file is on [Custom specialists](../60-custom/specialists.html).

| Field | Type | Engine default | What it does | Rule |
|---|---|---|---|---|
| `speciality` | Speciality | "NONE" | The class tab, as a number | `0` to `5`; see [the classes](index.html#the-six-classes). Never `6`. |
| `cost` | int | 0 | Hiring price | Shipped specialists cost 500 to 3,000. |
| `uiName` | string | — | Name on the card | 20 characters including spaces. This limit is real. |
| `uiDesc` | string | — | Story on the card | Saber says 280 characters; not enforced. 519 characters rendered in full. |
| `bage` | string | "specChemistBadge2" | Square portrait | 364 x 364 PNG with alpha. File name without folder or `.png`. |
| `bg` | string | "specSlotContent" | Wide strip | 380 x 92 PNG with alpha. |
| `bgSmall` | string | "specSlotContentSmall" | Small strip | 124 x 52 PNG with alpha. |
| `modifiers` | collection | — | The abilities | A list; see [Every ability](modifiers.html). |
| `isLocked` | bool | — | Hidden until unlocked by an objective reward | Leave `false`. Unlocking a custom one is untested. |
| `isDlc` | bool | — | Tied to a paid DLC | Working mods write this as `isLockedByDlc: false`. Leave it false. |
| `rang` | int | 0 | Unused | Saber marks it unused. Leave `0`. |
| `upgradeToUnlock` | string | — | Unused | Saber marks it unused. Leave `""`. |

The defaults matter when a field is left out. The portrait defaults are
vanilla placeholder symbols, so a missing portrait shows a stock picture, not
an error.

Saber's guide also lists `dbg_hided`, a debug switch that hides the specialist
from the recruitment screen and is slated for removal. It isn't in the
engine's field list. Don't set it.

## A minimal descriptor

```json
{
    "SslType": "SpecialistDesc",
    "SslValue": {
        "name": "SpecialistSettings",
        "speciality": 0,
        "rang": 0,
        "cost": 1600,
        "isLocked": false,
        "isLockedByDlc": false,
        "upgradeToUnlock": "",
        "uiName": "What the crew calls them",
        "uiDesc": "The story shown on the card.",
        "bage": "myguy_bage",
        "bg": "myguy_bg",
        "bgSmall": "myguy_bgSmall",
        "modifiers": []
    }
}
```
