---
title: Porting a SnowRunner truck
part: Vehicles
order: 650
summary: SnowRunner and Expeditions share the mod format, so a SnowRunner vehicle's meshes load untouched. Its textures do not, and that is why ported trucks come out solid black.
---

# Porting a SnowRunner truck

Expeditions and SnowRunner are both Saber engine games and they share one mod
format. Saber's own documentation covers truck modding for both titles in a
single section, which tells you how close they are.

So a SnowRunner vehicle mod can be brought into Expeditions. People already do
it — BFW, iX-5 and ULM C10 are community ports. But there is one asymmetry that
costs most people their first attempt, and it is worth understanding before you
start.

## The one thing that breaks

**Meshes port untouched. Textures do not.**

A published mod contains compiled geometry and converted textures. The geometry
is cross-compatible: drop a SnowRunner truck into Expeditions and it will spawn,
drive, steer and articulate its suspension perfectly.

Its textures will not load, and the vehicle renders **solid black** — body,
glass, wheels, everything. The log says:

```
Failed to load texture textures/<modid>\trucks/carroceria__d_a.tga
```

The reason is that the mod's `.pct` textures were encoded by SnowRunner's
converter, and Expeditions cannot decode them. When a texture fails, the engine
falls back to looking for the source `.tga`, which a packed mod never ships. So
every material on the vehicle ends up with no albedo at all.

<span class="prov prov-unver">measured</span>
The `.pct` container header is **byte-identical** between the two games: magic
`TCIP`, version 258, header size 32, same width and height fields. You cannot
tell a SnowRunner texture from an Expeditions one by looking at it. The truck
going black is the only symptom you get.

## What is not the cause

This took two days to find, and the reason is that the mod looks correct in every
respect that is easy to check. If your truck is black, **do not** go looking at:

pak layout · file naming · letter case · the mod id · `modio.json` fields ·
`modStateList` · `signature.cache` · texture dimensions · missing material
targets · the mesh container · customization presets

Every one of those was tested against a working mod on the same install, and
every one had a counterexample — a mod that got it "wrong" and rendered fine.
None of them matter. The problem is in the texture payload bytes.

Equally, **do not try to decode the `.pct`**. The payload is the right size for
BC3 with a mip chain but is swizzled or proprietary; a correct BC3 decode scores
under 15 mean error against a known source image, and every byte offset in the
file scores about 66, which is noise. `--extract-textures` also returns nothing
useful. You do not need to decode anything — you re-encode instead.

## The fix

Hand Expeditions textures that **its own encoder** produced. The game ships that
encoder: `Sources\Bin\ResourceConverter.exe`.

The whole process is: work out which textures the mod's materials ask for, write
a source `.tga` for each one, run them through the converter, put the results
back into `pc.pak`, and install.

### With the tool

```
python F:\Expeditions\Toolkit\port_vehicle.py analyze <mod.zip>
python F:\Expeditions\Toolkit\port_vehicle.py port <mod.zip> --id <modid> --name "My Truck"
```

Run `analyze` first. It tells you how many materials it has a colour for, which
ones it does not, and which materials the mod's author declared but never
actually put in the mesh.

`port` then does the rest and installs to `.modio\mods\<id>\`. See
[the AI tools section](../80-ai-tools/toolkit.html) for the flags.

### By hand

The invocation has two traps in it, and both produce errors that point at the
wrong thing:

```
ResourceConverter.exe --all-pct -s -r <modRoot> -i textures/trucks/X.tga -o prebuild/textures/pct/trucks_X.pct
```

* **`-i` is resolved relative to `-r`.** Give it an absolute path and it answers
  `Unable to find texture file <path>` about a file that is plainly sitting
  there. The message means "not underneath `-r`", not "does not exist".
* **`-o` is resolved against the working directory**, not `-r`. The output lands
  next to the executable in `Sources\Bin\prebuild\`. Collect it from there and
  delete the folder — it is inside your game install.
* **`-s` is not optional.** Without it, an assert can open a modal dialog on your
  desktop and wait for a click that never comes.

Then rebuild `pc.pak` with the new `.pct` files in `prebuild/textures/pct/`, and
install three files to `.modio\mods\<id>\`: `<Name>.pak`, a file named literally
`pc.pak`, and `modio.json`.

!!! warning "Write zero extra fields when you repack"
    `pc.pak` is a plain zip, but Python's `zipfile` copies `ZipInfo.extra` into
    the **local** header as well as the central directory, and the engine then
    fails to read that member. Build fresh `ZipInfo` objects. Validate by
    inflating every member afterwards.

## Always test the encoder before you trust it

The game's sample mod — the one TOOLS → Add Mod generates — ships both the source
`.tga` files *and* the `.pct` files the game produced from them. That is a free
ground truth.

Re-encode one of its source textures and compare against the game's own output.
It should come out **byte-identical**. If it does not, stop; something about your
invocation is wrong and nothing downstream will work.

`port_vehicle.py` runs this check automatically and refuses to continue if it
fails.

## What you will and will not get

Re-encoding fixes the *encoding*. It does not recover the original artist's work,
because that art only exists inside the undecodable `.pct` files.

If you generate flat colours from material names, you get a clean, correctly
coloured vehicle with working paint, glass and lights — not the author's livery,
logos or panel wear. If you want the real appearance, ask the mod's author for
their source `.tga` files and pass them with `--donor`.

## The errors you can ignore

```
Mesh| Cant find material's part by name 'negrochasis' in trucks_<name>_<modid>
```

<span class="prov prov-doc">documented</span>
`<Material Name="...">` must match the name of a material **in the FBX file**.
Mod authors routinely declare materials their geometry does not contain —
including, in one real case, the same material misspelled and shipped both ways.

These are the author's own defect and they are **cosmetic**. A known-good,
perfectly rendering mod on the same install ships three of them. They are not why
your truck is black, and fixing them will not change anything.

## Checking your work

After a launch, read `base\logs\LegacyLog.txt`. `Failed to load texture` should
be **zero**.

!!! note "A clean log proves nothing on its own"
    If you are comparing against another mod that works, first check that mod is
    mentioned in the log **at all**. A short launch-and-quit may never have
    loaded it, and its silence then means nothing.
