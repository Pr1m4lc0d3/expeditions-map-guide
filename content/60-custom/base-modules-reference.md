---
title: Every base module, and every surface you can edit
part: Custom content
order: 625
summary: The fourteen built-in base modules, what each descriptor field does, every image slot and where it appears on screen, and the values the engine actually accepts.
---

# Every base module, and every surface you can edit

A base module is a thing the player buys at a deploy zone: a repair station, a
fuel station, a workshop. This page is the reference for all of them — what the
built-in ones are, which fields you can set, which pictures appear where, and
what values the engine will accept.

Everything on this page was read out of the shipped game — the field names and
their types come from the editor's own type definitions, and the artwork names
come from the game's UI bundle. Where something is measured rather than
documented, it says so.

## The fourteen built-in modules

These are the families that ship with a complete set of artwork. The names in
the right-hand columns are UI symbols, not files — they live inside the
Scaleform bundle, and a descriptor refers to them by name.

| Family | Popup card | List row | Small row | Map icon | Trade icon |
|---|---|---|---|---|---|
| Base station | `moduleBaseStationPopup` | `moduleBaseStationRight` | `moduleBaseStationSmall` | — | — |
| Com center | `moduleComCenterPopup` | `moduleComCenterRight` | `moduleComCenterSmall` | — | — |
| Double stock | `moduleDoubleStockPopup` | `moduleDoubleStockRight` | `moduleDoubleStockSmall` | `moduleDoubleStockMap40` | `moduleDoubleStock48` |
| Drone base | `moduleDroneBasePopup` | `moduleDroneBaseRight` | `moduleDroneBaseSmall` | — | — |
| Evacuator | `moduleEvacuatorPopup` | `moduleEvacuatorRight` | `moduleEvacuatorSmall` | — | — |
| Extra storage | `moduleExtraStoragePopup` | `moduleExtraStorageRight` | `moduleExtraStorageSmall` | `moduleExtraStorageMap40` | `moduleExtraStorage48` |
| Gas station | `moduleGasStationPopup` | `moduleGasStationRight` | `moduleGasStationSmall` | `moduleGazStationMap40` | `moduleGazStation48` |
| Generator | `moduleGeneratorPopup` | `moduleGeneratorRight` | `moduleGeneratorSmall` | `moduleGeneratorMap40` | `moduleGenerator48` |
| Helicopter | `moduleHelicopterPopup` | `moduleHelicopterRight` | `moduleHelicopterSmall` | `moduleHelicopterMap40` | `moduleHelicopter48` |
| Parking | `moduleParkingPopup` | `moduleParkingRight` | `moduleParkingSmall` | `moduleParkingMap40` | `moduleParking48` |
| Repair station | `moduleRepairStationPopup` | `moduleRepairStationRight` | `moduleRepairStationSmall` | `moduleRepairStationMap40` | `moduleRepairStation48` |
| Resource zone | `moduleResourceZonePopup` | `moduleResourceZoneRight` | `moduleResourceZoneSmall` | — | — |
| Service station | `moduleServiceStationPopup` | `moduleServiceStationRight` | `moduleServiceStationSmall` | `moduleServiceStationMap40` | — |
| Workshop | `moduleWorkshopPopup` | `moduleWorkshopRight` | `moduleWorkshopSmall` | `moduleWorkshopMap40` | `moduleWorkshop48` |

!!! warning "The gas station is spelled two different ways"
    Its backgrounds are `moduleGa**s**Station…` and its icons are
    `moduleGa**z**Station…`. That is Saber's own inconsistency, it is in the
    shipped bundle, and a name built by pasting the family prefix onto `Map40`
    will silently resolve to nothing. **Never construct a symbol name by
    concatenation. Copy it from the table.**

A dash means the game does not ship that symbol for that family. It is not an
error to leave the matching field empty — the engine falls back to the default
in the field table below.

## The module identifiers

`zoneProperty.moduleId` is the module's identity. These are the values the
built-in modules use:

```
ANTENNA          DOUBLE_STOCK     EXTRA_STORAGE    GENERATOR
BASE_MODULE      DRONE_BASE       GAS_STATION      HELICOPTER
PARKING          REPAIR_ZONE      SERVICE_STATION  SUPPLY_SHOP
TOW_TRUCK        WORKSHOP
```

!!! danger "Reusing an identifier another mod holds empties the whole panel"
    The Base modules panel comes up **completely blank**, with the raw key
    `UI_BASE_BUILDING_SUBHEADER` where its heading should be. No crash, no log
    line, nothing in `LegacyLog.txt`.

    Measured 2026-10-16: three mods had been colliding with *vanilla*
    identifiers for weeks with a working panel. It broke only when a second
    *mod* took `DOUBLE_STOCK`. Two shapes are known to work — an off-table id of
    your own, or no `moduleId` at all.

## The models

A module has **four** model slots, and the one the player sees depends on where
they build it.

| Field | Used when | Notes |
|---|---|---|
| `modelId` | main base | the medium model |
| `modelIdAdditional` | outpost | the **small** model |
| `modelAnimated` | main base, while building | the build animation |
| `modelAdditionalAnimated` | outpost, while building | |

`defaultDeployPoint` on the deploy zone decides which pair is used. Twelve of
the thirteen built-in families ship a `small_` twin; `fob_module_storage` has
none.

!!! warning "Replace only the medium model and every outpost stays vanilla"
    This is the most common surprise. If your module appears correctly at a main
    base and as a stock amber box at an outpost, you set `modelId` and left
    `modelIdAdditional` pointing at the built-in model.

Built-in model names follow `models_fob_module_<family>` with a `small_` prefix
for the outpost variant and an `_objective` suffix for the animated one:

```
models_fob_module_extra_storage                 medium, finished
models_fob_module_extra_storage_objective       medium, building
models_fob_module_small_extra_storage           outpost, finished
models_fob_module_small_extra_storage_objective outpost, building
```

## Every field you can set

All 34 authorable members of `BaseUpgradeDesc`, from the engine schema.

### Identity and text

| Field | Type | Default | What it is |
|---|---|---|---|
| `uiName` | string | — | the name in the list and on the card |
| `uiDesc` | string | — | the flavour paragraph on the card |
| `uiDescTradeHeader` | string | — | heading on the trade panel |
| `uiTradeDefaultDescText` | string | `UI_POPUP_TRADE_MODULE_DEFAULT_DESC` | fallback trade text |

### Money

| Field | Type | Default | What it is |
|---|---|---|---|
| `cost` | int | `0` | build price |
| `sellPrice` | int | `0` | refund when sold |

### Behaviour

| Field | Type | Default | What it is |
|---|---|---|---|
| `isInteractive` | bool | `True` | **`False` makes the module inert** — it builds and does nothing |
| `isLockedByDefault` | bool | `False` | hidden until unlocked |
| `isOnlyOneAvailableAtDeployZone` | bool | `False` | one per zone |
| `availableViaDroneDelivery` | bool | `True` | orderable by drone |
| `isFromMod` | bool | `False` | set by the loader, not by you |

### Models

| Field | Type | Default | What it is |
|---|---|---|---|
| `modelId` | string | — | medium model brand |
| `modelIdAdditional` | string | — | small model brand |
| `modelAnimated` | string | — | medium build animation |
| `modelAdditionalAnimated` | string | — | small build animation |
| `modelOffset` | mod | null | position nudge |
| `modelAdditionalOffset` | mod | null | position nudge, small |
| `modelYRotation` | float | — | facing, degrees |
| `modelAdditionalYRotation` | float | — | facing, degrees, small |
| `animationStagesProgress` | int | — | build stage map, e.g. `{stage_0: 0, stage_1: 1}` |
| `animationAdditionalStagesProgress` | int | — | the same for the small model |

### The zone

| Field | Type | Default | What it is |
|---|---|---|---|
| `zoneProperty` | mod | null | what the module *does*. See below. |
| `soundsFadeParams` | mod | null | audio fade |

## Every picture, and where it lands

Eleven fields take an image. This is the part that is easiest to get wrong,
because a wrong name does not fail loudly — it draws a placeholder.

| Field | Default | Where it appears |
|---|---|---|
| `bg` | `moduleSlotContent` | the wide artwork in the list row |
| `bgRight` | `moduleSlotContentRight` | the row when the panel is right-aligned |
| `bgSmall` | `moduleSlotContentSmall` | the compact row |
| `popupModuleBg` | `""` | the big picture on the build card |
| `iconMap40` | — | the 40 px marker on the map |
| `iconTrade` | — | the 48 px icon on the trade panel |
| `icon20` | — | 20 px, inline |
| `icon40` | — | 40 px, inline |
| `iconModuleBg` | `""` | icon plate behind the glyph |
| `tradeArrowsSpecialIcon` | `""` | the arrows on a trade row |
| `uiDescTradeHeaderIcon` | — | glyph beside the trade heading |

A list row is **778 × 255 px** in a 3840 × 2160 frame: a title strip about 55 px
tall carrying the name, the price and the small glyph, with the `bg` artwork
filling the roughly 200 px beneath it. The stock rows are down the left of this
capture (1), and the card in the middle (2) is what `popupModuleBg` fills:

![Stock store rows and the Repair station build card](../assets/bases/repair-station_placement.png)

Every built-in module's own rows and card are on its page in
[Appendix A](../62-modules/gas-station.html).

!!! warning "Composition, not just size"
    The artwork is **left-anchored and fills the row height**, and it clips off
    the left edge. A picture that is centred with margins reads as too small and
    floats in the middle of the row. Match the framing of the vanilla rows
    above, not just their pixel dimensions.

### Download the template

!!! note "Start from the template, not from a blank canvas"
    [**expeditions-module-art-template.zip**](../assets/downloads/expeditions-module-art-template.zip)

    Four correctly named transparent canvases at the exact sizes, four guide
    sheets showing which part of each the game crops or covers, a README, and a
    descriptor snippet you can paste. Rename `MODNAME` to your module and paint
    inside the blanks.

### Supplying your own pictures

A mod ships PNGs in `ui/textures/` and names them in the descriptor **without
the extension and without the folder**:

```
ui/textures/mymodule_bg.png        ->   "bg": "mymodule_bg"
ui/textures/mymodule_popup.png     ->   "popupModuleBg": "mymodule_popup"
```

!!! danger "Only bg, bgRight, bgSmall and popupModuleBg may be custom PNGs"
    The icon fields take **UI symbol names from the game's bundle**, not files.
    Pointing `iconMap40` at a PNG you shipped does not work. Use a vanilla
    symbol from the table at the top of this page.

    A field naming something that is neither a shipped symbol nor a PNG in your
    mod draws a placeholder: a small yellow square with a red mountain in it.
    If you see that, the name is wrong.

## What the module does: `zoneProperty`

The descriptor describes the *thing*; `zoneProperty` describes its *function*.
The engine knows 72 zone-property types. These are the ones a base module uses:

| Type | Key members | Use |
|---|---|---|
| `ZonePropertyFobModuleStorage` | `moduleId` + all of inventory storage | anything that holds or trades goods |
| `ZonePropertyFobModuleDefault` | `moduleId` | a module with no inventory |
| `ZonePropertyFuelStation` | `pricePerLiter` | engine-keyed fuel point |
| `ZonePropertyGenerator` | `exchangeRate`, `fuelAmountForOneConvert`, … | fuel to electricity |
| `ZonePropertyHelicopter` | `moduleId`, `transferCost` | transport |
| `ZonePropertyBaseBuilding` | `modelPlacementZone` | where a module may be placed |
| `ZonePropertyDeploy` | `fobModulesZones`, `defaultDeployPoint`, `maxTrucksNum` | the deploy zone itself |

!!! danger "Most of these are engine-keyed and inert for a mod"
    `ZonePropertyFuelStation`, `ZonePropertyServiceStation` and
    `ZonePropertyFobModuleDefault` are wired to built-in behaviour. A **mod**
    using them gets a module that builds and then does nothing at all.

    Measured: a custom fuel station built on `ZonePropertyFuelStation` was
    completely inert. Rebuilt on `ZonePropertyFobModuleStorage` with a single
    fuel slot, it worked.

    The antenna is the same story in a different place: an `AntennaUpgradeDesc`
    mod builds and sells but never reveals an air drop, even with the game's
    script patched. See [Intelligence center](../62-modules/com-center.html#building-your-own-the-ability-does-not-work).

    ⇒ **For a mod, use `ZonePropertyFobModuleStorage` and shape it with slots.**

### Shaping a storage module

`ZonePropertyFobModuleStorage` inherits all of `ZonePropertyInventoryStorage`:

| Member | Type | Default | Meaning |
|---|---|---|---|
| `capacity` | int | `0` | general cargo slots |
| `heavyInvCapacity` | int | `0` | heavy cargo slots |
| `slotsSettings` | ZoneItemSlot | — | explicit slot list |
| `fuelSlotSettings` | mod | null | the fuel slot |
| `repairsSlotSettings` | mod | null | repair points |
| `wheelsSlotSettings` | mod | null | tyres |
| `electroSlotSettings` | mod | null | electricity |
| `expandedConsumablesCapacity` | float | `3` | |
| `alwaysSpawn` | bool | `False` | |
| `isAtDeployZone` | bool | `False` | set `True` for a base module |
| `allowPutConsumablesToHeavyInv` | bool | `False` | |
| `isModelBreakageQuestProp` | bool | `False` | |
| `isAffectedByAdditionalOutpostResourcesAbility` | bool | `False` | specialist perk |
| `isAffectedByAdditionalAirdropResourcesAbility` | bool | `False` | specialist perk |
| `isShown` | bool | `True` | |
| `isAffectedByZoneSettings` | bool | `True` | |
| `zoneDiscoverability` | mod | null | |
| `model` | mod | null | |

A slot is a `ConsumablesSlot`:

```json
{ "$type": "ConsumablesSlot",
  "quantity": 1200,
  "chance": 1,
  "tradeFromTruckToZone": false }
```

!!! note "`tradeFromTruckToZone` decides which way goods move"
    `false` — the zone gives to the truck. This is a shop or a fuel pump.
    `true` — the truck gives to the zone. This is a depot or a delivery target.

    A fuel station that will not dispense usually has this the wrong way round.

**To build a fuel-only module**, set `capacity` to 0, leave `slotsSettings`
empty, null the repairs, wheels and electro slots, and give it only
`fuelSlotSettings` with `tradeFromTruckToZone: false`. Verified working in game.

## Checking your work

Before you deploy, check the things that fail quietly:

- **The descriptor** — every image name is either a symbol from the table at the
  top of this page or a PNG you actually shipped in `ui/textures/`, and your
  `moduleId` is not one another mod already holds.
- **All four model slots** — not just `modelId`. An outpost uses
  `modelIdAdditional`, and leaving it unset is why a module looks right at a
  main base and vanilla at an outpost.
- **Every level of detail, not just the full-detail mesh.** The game draws the
  reduced versions at normal viewing distance, and each one is simplified
  separately. A model whose texture looks right close up can be wrong a few
  metres away, so look at it from a distance as well as up close.

!!! warning "A clean check is not proof"
    Every check above can pass on a module that still looks wrong in game. The
    arbiter is the running game. Deploy it and look at it.
