---
title: Gateways between maps
part: Zones
order: 460
summary: How to link two custom maps so a truck drives from one to the other, which Saber's guide says is not supported.
status: draft
---

A gateway is a zone that sends the player's truck to a zone on another map. It is
how vanilla joins a surface map to its cave.

Saber's guide says custom regions of several linked maps are not supported in
Expeditions. <span class="prov prov-doc">documented</span> **They can be made to
work.** A truck has driven from one custom map to a second and back again, on
PC. <span class="prov prov-unver">tested in game</span> The game has all the
parts. Saber's tools just don't produce a working result by themselves.

!!! warning "This page is a draft"
    One two-map test proves it can be done. It does not yet prove every step below
    is needed, and the list at the end says what has not been tested.

## What you need

- Two maps, each packed to a `.pak`, each with a deploy zone.
- A gateway zone on each map, each pointing at the other.
- A small region folder that names both maps.

## Step 1: give each map four built-in ground layers

Do this first, because getting it wrong crashes the game the moment a truck
arrives, and the error says nothing useful.

A map's material needs its layers filled in, and **the base layer must be a
built-in tile**, not a custom one. Saber's guide says a new material has four
layers, and every working map checked has four in its source file.
<span class="prov prov-doc">documented</span>

A custom tile can be left out of the compiled map without warning. A map whose only
layer was a custom tile compiled with **zero** ground layers. The game asks what
surface a truck is standing on, finds an empty list, and crashes.
<span class="prov prov-unver">measured</span> In the editor that map drew black and
could not be painted, so **black ground is your warning sign.**

## Step 2: place the gateway zones

Place a zone on each map and give it a `ZonePropertyGateway` prop. The tested zones
were round, 30 m across. Keep the target zone clear of models and plants with
collision, because trucks arrive inside it. <span class="prov prov-doc">documented</span>

| Field | What to set |
|---|---|
| `levelZoneLink` | the target, see step 3 |
| `cameraDir` | any non-zero direction, such as `1, 0, 0`. All zeros gives a black screen <span class="prov prov-doc">documented</span> |
| `cameraPos` | where the arrival camera starts |
| `animationTime` | length of the arrival camera move in milliseconds. The test used 3000 |
| `isShown`, `isAffectedByZoneSettings` | `true` |

Both zones need the prop. Saber warns that a gateway whose partner has no
`ZonePropertyGateway` crashes during the transfer.
<span class="prov prov-doc">documented</span>

## Step 3: write the link with the real level name

This is the step that made the crossing work. Once a map is installed, the game
calls it `mod_level_<name>`, not `level_<name>`. The link has to use that name:

```
mod_level_gate_two || gate_two
```

The part before `||` is the level. The part after is the zone on that level.

**Packing rewrites this line.** The packed map's `zone_settings.json` comes out as
`level_gate_two || gate_two`, a level that doesn't exist. Each pack needs the link
corrected inside the `.pak` afterward. <span class="prov prov-unver">tested in game</span>

Two wrong forms, and what they do:

| Link | Result |
|---|---|
| `level_gate_two \|\| gate_two` | names a level that doesn't exist |
| `` ~#@%$`*level_gate_two~#@%$`* \|\| gate_two `` | the prompt shows the raw text, and pressing Let's go drops you to the main menu <span class="prov prov-unver">tested in game</span> |

That second form is what Saber's region tool writes. It does work inside the region
files, where the game swaps it for the real name as it loads them. It isn't swapped
in a map's own `.pak`, and in the test the map's own copy is the one the game used.
<span class="prov prov-unver">measured</span>

## Step 4: add the region folder

The game looks for regions in `Media\prebuild\<region name>\`, with a
`regionDesc.json` in it. <span class="prov prov-unver">measured</span> Saber's tool
for making one is hidden inside `ZoneSettingsEditor.exe`, and what it writes needs
fixing by hand. Do not save through the tool again afterward, because it strips
values the game needs.

The region's `zone_settings.json` needs all of these, or the game fails in a
different place for each one <span class="prov prov-unver">measured</span>:

| Requirement | If it's missing |
|---|---|
| The data key and region name are `mod_region`, not your region's name | the game stops before the main menu |
| Every map after the first has `modId` and `inventorySettings` | the Custom list comes up empty |
| Every map has `uiFuelConsumptionModifier` 1, `birdsMultiplier` 0.5, `noFlyZone` -1 | a blank expedition setup screen |
| Every map has a `caveSettings` block and a `uiImages` list | the game freezes on arriving at the map |
| Gateways have `isShown` and `isAffectedByZoneSettings` set to `true` | the tool strips these and the region loader doesn't restore them |

Whether the crossing needs this folder at all is not yet tested, see below.

## What the player sees

Drive into the zone and a **Travel to** prompt appears. Press it, and a popup offers
**Let's go** and **Not now**. The truck then arrives in the target zone, and the
gateway on that side brings it back.

![A truck inside a gateway zone on the first test map, with the Travel to Gate Two prompt at the bottom of the screen](../assets/gateways/travel-prompt-gate-one.jpg)

![The same truck after crossing, on the second test map, whose ground is painted green, with a Travel to Gate One prompt](../assets/gateways/arrived-gate-two.jpg)

The popup needs two images, `Size_800x520` and `Size_800x520_Gray`, in `uiImages`.
<span class="prov prov-doc">documented</span> Without them it shows an empty picture
and logs an error, but the crossing still works.
<span class="prov prov-unver">tested in game</span>

## Not yet known

- Whether the region folder is needed, or the two `.pak` files are enough.
- Whether a `mod_level_` link can be kept through a pack, so that no correction is
  needed afterward.
- How to deliver a linked set of maps to other players, and whether a map installed
  through mod.io still goes by `mod_level_<name>`.
- Whether a cave works. Vanilla caves use `caveSettings`, with `isCave` and
  `surfaceMapID`, and `isCave` on the gateway. None of that has been tried on a
  custom map.
- More than two maps, or more than one gateway on a map.
- Popup images, locked gateways, modded trucks, and anything carried across.
- Any platform other than PC.
