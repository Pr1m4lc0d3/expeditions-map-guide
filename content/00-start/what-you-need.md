---
title: What you need
part: Start here
order: 110
summary: The tools, the folders, and an honest note on how long each part of the job actually takes.
---

## The tools

Everything you need ships with the game. There is nothing to buy and nothing to
download.

| Tool | Where | What it does |
|---|---|---|
| **Map editor** | `Sources\BinEditor\ExpeditionsEditor.exe` | terrain, objects, roads, water, and placing the zones |
| **Zone settings tool** | `Sources\BinEditor\ZoneSettingsEditor.exe` | the properties **on** those zones, plus all objectives. Opens from the editor's toolbar |
| **Resource converter** | `Sources\Bin\ResourceConverter.exe` | converts and compiles assets |
| **Type schema** | `Sources\BinEditor\meta_desc_ssl.ps` | not a tool, a text file. Every type the editor understands, and the final word when a guide and the game disagree |

Two of those deserve a note.

**The zone settings tool is a separate program.** This confuses people, because
"zones" feel like a map thing. You place the zone's *shape* in the map editor, and
you set what that zone *does* in the zone tool. Two programs, one concept.

**The schema is worth knowing about.** It is a plain text file listing every field
the editor understands. When the official guide says a feature does not exist, the
schema sometimes disagrees, and the schema is what the software actually runs on.

## Your working folders

Under `Documents\My Games\Expeditions\Media\`:

```
Media\
  prebuild\<level>\      your source. this is where you work.
  levels\<Level>\        staging. the zone tool reads from here.
  Mods\<Level>.pak       the packed map. the game reads only this.
```

The relationship between those three is the most important thing on this site, so
it gets [its own page](where-things-live.html).

## How long things take

Worth knowing up front, because two of these are much slower than people expect
and it changes how you plan a session.

| Job | Roughly |
|---|---|
| Open a map in the editor | seconds to a minute, depending on size |
| Sculpt terrain, place objects | as long as you like, it is interactive |
| **Pack the map** | **around 25 minutes** |
| Load the packed map in game | a minute |

That 25 minutes is the number that shapes everything. It means **a
trial-and-error loop through the game costs you half an hour per attempt.** So the
skill that matters most is not sculpting, it is catching mistakes before you pack.

A long pack is not a hang. It builds output for six platforms in sequence. Let it
finish.

## What you can and cannot do outside the editor

Some of a map is stored as plain text you can read and edit. Some is not.

**Editable by hand:** zones and their properties, objectives, contracts, tasks,
rewards, level metadata, starting money and prices. These are JSON files, and
scripting them is often faster and safer than clicking.

**Editor only:** terrain shape, the *position* of anything, roads and rivers,
object placement, textures and vegetation. These live in compiled scene data. You
can automate what goes *into* the editor, but the placement itself happens there.

This split is why a zone has two halves. The shape is editor work. The behaviour
is a text file.

## A note on backups

Keep one, and keep it current.

Map data is large. A single packed map can run to hundreds of megabytes, and the
staging folder holds uncompressed texture masters that are larger still. It is
very easy to write a backup on every save, forget about it, and discover later
that you have filled a drive with near-identical copies of the same map.

One backup. The latest. Overwrite it. And never put a backup inside a folder the
editor scans, because it will try to load it as map content.
