---
title: Service station
part: Appendix A - base modules
order: 905
summary: Lets trucks in its area spend spare parts on armor, up to 20% above full strength.
verdict: works
verdict_text: "A custom one builds, and trucks in its area can add armor up to the same +20% as the vanilla module. Tested in game, October 2026."
---

# Service station

![Service station store card](../assets/bases/service-station_card.png)

Lets a truck parked in its area spend spare parts on armor: strength above 100% on the engine, gearbox, suspension and fuel tank.

## How it works

Nothing happens at the module itself. The vanilla one has no trade screen (`isInteractive` is false) and holds no stock. It only raises the armor cap of a truck standing in its area.

The player adds armor the same way they repair. Open the vehicle status panel, select a part, and spend spare parts on it. The game's Codex describes it: some specialists and base modules raise a part's strength limit, and while that extra strength lasts, collision damage is reduced.

| Situation | Highest a part can reach |
|---|---|
| No armor specialist, away from the station | 100% (repair only) |
| No armor specialist, in the station's area | 120% |
| A specialist with +95% armor, away from the station | 195% |
| The same specialist, in the station's area | 215% |

Measured in game, October 2026. The station's +20% adds to whatever the team's specialists give.

!!! note "Where armor can be added"
    In the test above, the specialist's +95% could be added away from any station, and that specialist does **not** have the `ArmorRestoreEverywhere` modifier. Only the station's own +20% needed the truck to be in its area. Saber's specialist docs give an example that reads as if adding armor away from a station needs `ArmorRestoreEverywhere`. What that modifier adds on top has not been tested.

!!! warning "The +20% cannot be changed by a mod"
    `ZonePropertyServiceStation` has no strength setting. Its only members are `moduleId`, `zoneDiscoverability` and two inherited switches. The +20% is the game-wide `baseArmorMultiplier` (default `0.2`) on `TruckArmorController`, compiled into the game's own data.

    Raising it would mean patching the game itself, for every truck at every station, vanilla included. So a custom service station can differ only in price, models and art.

    To give players more armor, use specialists. The `ArmorCapacity` modifier adds a percentage to each of the four parts. See [Specialists](../60-custom/specialists.html).

## In game

**The purchase card.** This is what a player sees before buying.

![Service station purchase card](../assets/bases/service-station_buy.png)

Below the description it shows: Four part-type glyphs. No numbers.

That is **not an image and not a field you set**. It is drawn by the engine. `ZonePropertyServiceStation` has four members and **none of them is an item list**. A custom module gets this row only by using the same zone property type; there is no way to choose which glyphs appear.

**The module once built.** This is the panel the player opens at the base.

![Service station in use](../assets/bases/service-station_owned.png)

If your module does not produce a panel like this one, it is not configured correctly. The numbers here and the numbers on the purchase card are the same values, read from the same place.

!!! note "Documented for custom modules"
    Saber's own documentation lists this module's zoneProperty and says these props exist to configure CUSTOM FOB modules.
    Use the property named below, not one you inferred from a symbol name.

## Identity

| | |
|---|---|
| `zoneProperty.moduleId` | `SERVICE_STATION` |
| Zone property | `ZonePropertyServiceStation` |
| Its members | engine-keyed |

## Models

| Slot | Model |
|---|---|
| `modelId` (main base) | `models_fob_module_service_station` |
| `modelIdAdditional` (outpost) | `models_fob_module_small_service_station` |
| `modelAnimated` | `models_fob_module_service_station_objective` |
| `modelAdditionalAnimated` | `models_fob_module_small_service_station_objective` |

## Artwork: every image slot

Six images appear per module, in six different places. They are
separate images, not one picture reused.

| Where you see it | Field | Falls back to | Symbol for this module |
|---|---|---|---|
| Store sidebar, the list row | `bg` | `moduleSlotContent` | `moduleServiceStation` |
| Store card, when you select it | `popupModuleBg` | (none) | `moduleServiceStationPopup` |
| Right card, when the module is used | `bgRight` | `moduleSlotContentRight` | `moduleServiceStationRight` |
| HUD strip of deployed modules | `bgSmall` | `moduleSlotContentSmall` | `moduleServiceStationSmall` |
| **On the map** | `iconMap40` | (none) | `moduleServiceStationMap40` |
| Trade panel glyph | `iconTrade` | (none) | `(none ships)` |

!!! warning "How much of that is confirmed"
    The **fallbacks** are the engine schema defaults, so they are fact.
    The **symbols** in the last column are confirmed to exist in the
    game's UI bundle. Which field each one is wired to is **inferred
    from its suffix** and has not been verified against a module proven
    to work. Treat the last column as a strong lead, not as settled.

### Replacing them

!!! note "There is a template for this"
    [expeditions-module-art-template.zip](../assets/downloads/expeditions-module-art-template.zip) — the four
    canvases at the right sizes, named correctly, with the cropped and
    covered areas marked.

Three of the background images may be your own PNGs. Ship them at
`ui/textures/<name>.png` and name them in the descriptor **without the
folder and without `.png`**. These are the sizes mods on disk ship:

```
ui/textures/mymodule_bg.png       ->  "bg": "mymodule_bg"             380 x 92
ui/textures/mymodule_right.png    ->  "bgRight": "..."                760 x 90
ui/textures/mymodule_small.png    ->  "bgSmall": "..."                124 x 52
```

⛔ The two icons may not be your own files. `iconMap40` and `iconTrade`
take a symbol from the game's bundle; a PNG in an icon field does not
render. Borrow a vanilla symbol instead.

!!! note "The other five image fields"
    `icon20`, `icon40`, `iconModuleBg`, `tradeArrowsSpecialIcon` and
    `uiDescTradeHeaderIcon` are unset on every module examined, and take
    symbols only.

!!! warning "popupModuleBg can't be your own PNG"
    The game loads mod PNGs only for `bg`, `bgSmall` and `bgRight`. A mod
    PNG named in `popupModuleBg` draws the broken-image placeholder, a
    yellow square with a red mountain; that was seen in game. Set it to
    `""` or to a vanilla symbol such as the one in the table above. The
    module checker now reports a custom PNG here as an error.

### The four background images, rebuilt

Where each one is drawn, on the real screens:

![Service station slot placement](../assets/bases/service-station_placement.png)

The originals live inside the game's UI bundle and cannot be
extracted, so these are rebuilt from in-game captures. **Every one
below is a transparent PNG at the slot aspect — the same thing you
have to author.** The game supplies the brown row, the slate card and
the tan bar; your file supplies only the model.

!!! warning "These are FOUR separate images, not one image reused"
    Do not render your model once and drop the same picture into all
    four fields. Across the vanilla set the four differ in **crop,
    framing and left-to-right orientation**.

    **Three of the twelve are flipped in the store row**: Expanded
    parking, Cargo drone and Service station. The other nine run the
    same way in both slots.

    Those three have one thing in common. The feature that identifies
    the module sits on the LEFT of the purchase card — the parking
    barrier and cabinet, the drone itself, the hoist gantry — and the
    store row clips its left edge. Flipping is what saves that detail
    from the crop.

    **So the rule is: flip when the detail that identifies your module
    would otherwise be cropped away.** Decide it per slot by looking at
    what survives, not by reusing one render four times.

The slot sizes below are measured, not quoted: 762 x 184, 762 x 184,
1530 x 184 and 248 x 104 in a 2160p frame, which is exactly the
documented 380 x 92, 380 x 92, 760 x 90 and 124 x 52 doubled.

!!! note "Why bg shows the whole model when the game clips it"
    In game the store row cuts off the left of this art. That is the
    game drawing it, not your file — you author the complete model and
    let the row clip. The example below is the complete image.

`bg` — 380 x 92 — the store row **and** the sell dialog. Fills the row height and **clips off the left edge**.

![Service station bg](../assets/bases/service-station_bg.png)

⚠ **This module is one of the three whose store-row art is flipped**
relative to the purchase card. Compare the two images on this page
and you can see it directly.

`popupModuleBg` — 380 x 92 — the purchase card. The **whole model**, nothing cropped.

![Service station popup](../assets/bases/service-station_popup.png)

`bgRight` — 760 x 90 — the banner above the module card when it is in use. The artwork is **aligned to the RIGHT**; the icon and name sit on the tan bar to its left.

![Service station bgRight](../assets/bases/service-station_right.png)

`bgSmall` — 124 x 52 — the HUD strip of deployed modules. The **whole module**, scaled so it just fills the chip and touches its edges. Every vanilla chip is framed this way. Zooming in past that shows only a corner of the model and reads as far too big.

![Service station bgSmall](../assets/bases/service-station_small.png)

!!! note "Composition"
    Vanilla rows are **left-anchored**, fill the row height, and clip
    off the left edge. A centred picture with margins reads as too
    small and floats. Match the framing, not just the pixel size.

## Building your own

Saber's documentation names **`ZonePropertyServiceStation`** for this module.
A custom service station built on it works: trucks in its area can add armor up to +20%, the same as the vanilla module. Tested in game, October 2026.

Copy the vanilla one's behaviour: `isInteractive` false and `isOnlyOneAvailableAtDeployZone` true. The card's description should say what the player does, since nothing on the module shows it: park in the area, open the vehicle status panel and spend spare parts on armor.

Give it a `moduleId` **no other mod uses** — your own mod name works.

See [Module descriptor reference](../60-custom/base-modules-reference.html) for the full field list.
