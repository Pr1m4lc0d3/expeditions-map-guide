---
title: Sticker spots on mod trucks
part: Vehicles
order: 668
summary: How the garage's sticker menu decides where a sticker can go, and how to give a truck from a mod its own sticker spots with the sticker-spots tool and an AI assistant, checked by eye before anything is installed.
---

# Sticker spots on mod trucks

The trucks that came with the game each have a few fixed places for an exterior sticker: usually
both doors, the hood and the roof. Most truck mods have none, so their **Exterior stickers** menu
is empty. This page explains what a sticker spot is, then how to add your own spots to a mod
truck on your PC.

| You want | Use |
|---|---|
| Your own pictures as stickers on the trucks that came with the game | **Sticker Maker** on [mod.io](https://mod.io/g/expeditions/m/docs-rocks-sticker-maker). PC only, one installer |
| Sticker spots on a truck from a mod, for the stock stickers and your own | The [sticker-spots tool](https://github.com/Pr1m4lc0d3/expeditions-tools/tree/main/sticker-spots) in expeditions-tools, on this page |

> **Tested so far:** one pickup-truck mod, in game. All four spots took every stock sticker and
> My Sticker 1-10 and sat flat on the paint. Co-op with a partner who lacks the spots, and other
> body shapes, are not tested yet.

## What a sticker spot is

A sticker in this game is not painted on the truck. It is a small add-on: a thin, flat piece of
mesh that sits a few millimetres off the paint, with the sticker's picture as its texture. A
sticker spot is three things working together:

1. **A slot on the truck.** The truck's class lists it under `AddonSockets`, like any other
   add-on slot:
   ```xml
   <AddonSockets>
       <Socket Names="StickerSpots_MyTruck_door_r" />
   </AddonSockets>
   ```
2. **The sticker add-on that fits it.** Its class names the slot with `InstallSocket`, sets
   `Category="sticker_exterior"` (which puts it in the Exterior stickers menu) and points at its
   mesh. The mesh is the flat piece, already bent to the shape of the body under it.
3. **The list of pictures.** The mesh's header carries one `MaterialOverride` per sticker the game
   has, each swapping in a different picture. That list is what the menu shows when you pick
   the spot. A preset file under `classes/customization_presets/` ties the add-on to the game's
   `OutsideSticker1x1` template, the same one the stock trucks use.

The game draws the menu from those pieces alone, so a mod truck gets a working sticker menu as
soon as all three are in the truck's own mod. They have to be in the same mod as the truck: the
game files a mod's classes under its id, so a slot in one mod and a sticker in another never meet.

## Why a person has to place them

The mesh has to follow the body exactly, or the sticker cuts into the paint or floats off it. The
tool reads the body from the truck's own converted mesh and bends the flat piece onto it, so the
fit is automatic. **Where** the spot goes is not. A program can find a flat area, but it cannot
tell a door seam from a body line, or know that one door is an add-on the truck can lose. On a
four-door cab the first guess can land right across the gap between the doors.

So the tool never installs on its own judgement. It proposes spots, draws a picture of the
truck with every spot on it, and waits until you say it looks right.

## What you need

- Expeditions installed (Epic or Steam). The tool reads the game's sticker list from your own
  install, so it ships none of the game's files.
- The truck mod, installed through the game's mod.io browser and enabled.
- Python 3.10 or newer, and the tool:
  [sticker-spots](https://github.com/Pr1m4lc0d3/expeditions-tools/tree/main/sticker-spots). In
  its folder, `pip install -r requirements.txt`.
- An AI assistant that can run commands on your PC (optional, but it is what the tool is made
  for). Point it at the folder's `AGENTS.md`, which tells it the whole job and the rules.
- [Sticker Maker](https://mod.io/g/expeditions/m/docs-rocks-sticker-maker), if you want your own
  pictures (My Sticker 1-10) on the new spots too.

## Step by step

With an AI assistant, say **"add sticker slots to my &lt;truck&gt;"** and it runs these steps,
showing you each picture. Without one, run them yourself.

**1. Find the truck.**

```
python sticker_spots.py trucks
```

Each line is the `--mod` id and `--truck` name to use, with the mod's title.

**2. Scan it.**

```
python sticker_spots.py scan --mod <id> --truck <name>
```

It proposes up to four spots, `door_l`, `door_r`, `hood` and `roof`, and writes a plan and a
picture to `Documents\My Games\Expeditions\StickerSpots\`. The first scan of a detailed body can
take a few minutes. Every redraw after that takes a second or two.

**3. Read the picture.** It shows the truck from the left, the top and the right, shaded by the
angle of the surface. Door gaps, panel edges, badges, handles, vents and creases show as dark
lines. The rulers are in metres. Each spot is a box: green when it sits on clear paint, amber
when something is under it. The tool prints a `LOOK:` note for every amber box, for example:

```
door_r  right centre 0.94 0.80  size 0.60 x 0.60 m   LOOK: a line runs across it at y = 0.58, 0.62
```

Amber is not an error. A crease or a badge under a sticker may be fine to you. It is a reason to
look.

**4. Move the spots until they are right.**

```
python sticker_spots.py set  --mod <id> --truck <name> --spot door_r --centre 0.94 0.80
python sticker_spots.py set  --mod <id> --truck <name> --spot hood --size 0.6
python sticker_spots.py add  --mod <id> --truck <name> --spot tailgate --view top --centre -2.4 0 --size 0.5
python sticker_spots.py drop --mod <id> --truck <name> --spot roof
```

Each command redraws the picture. In the side views x runs along the truck (front is +x) and y
is height. In the top view x runs along the truck and y across it. To centre a spot on a door,
read the door's two edge lines off the ruler and take the middle. Mirror a door spot to the other
side by giving it the same numbers.

Good places, and places to avoid:

- **Doors:** the middle of one panel, clear of the door gap, the handle and the window.
- **Hood:** flat paint beside a scoop or bulge, not on it.
- **Roof:** clear of where a roof rack sits, or the rack hides it.
- **Never** on a part the truck can change in the garage, such as optional doors or a different
  hood. The sticker stays where the old part was and floats when the part changes or comes off.
- Sizes like the stock trucks' are a good start: about 0.5 to 0.6 m on a door, 0.6 to 0.8 m on a
  hood, up to 1.1 m on a roof. Stickers are square.

**5. Install it,** with the game and the map editor closed:

```
python sticker_spots.py install --mod <id> --truck <name>
```

The first install leaves a copy of the mod's file beside it, `<name>.pak.stickerspots_bak`.

**6. Check it in the game.** Garage, the truck, **Accessories > Exterior stickers**. Each new
spot lists every stock sticker, plus My Sticker 1-10 if Sticker Maker is installed. If a spot sits
off, close the game, `set` it, look at the picture, and `install` again. The new install replaces
the old spots.

## Taking them off

```
python sticker_spots.py remove --mod <id> --truck <name>
```

It removes exactly what `install` added. It refuses while a save has a sticker fitted on one of
the spots, because the save would then name a part that no longer exists. Take the sticker off in
the garage first.

## Things to know

- **A mod.io update of the truck replaces its files, and the spots go with it.** The plan is
  kept. Run `install` again after an update, before you load a save that has one of the stickers on.
- **The spots exist only on your PC.** In co-op, a partner without the same spots sees no
  sticker there.
- **Changing someone else's truck on your own PC is fine. Uploading it is not,** unless you made
  it or its licence allows it.
- The trucks that came with the game already have their spots. This tool does not change them.
  For your own pictures on those, use Sticker Maker.
