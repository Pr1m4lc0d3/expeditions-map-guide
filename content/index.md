---
title: Expeditions map making, for people who have never done it
part: Home
order: 100
summary: "A plain-language guide to building custom maps for Expeditions: A MudRunner Game. Start with a map that loads, then make it good."
---

# Make a map for Expeditions

Saber shipped a map editor with the game and a set of official guides to go with
it. The guides are accurate. They are also written field by field, in the order
the software stores things, which means you can read four pages about deploy
zones and still not know what a deploy zone is for.

This guide is the other way round. It explains what a thing **is** and what it is
**for**, then tells you which fields to fill in. It assumes you have never opened
the editor.

## Read this first if you read nothing else

Two rules save more time than everything else on this site combined.

1. **Get a map that loads before you make it pretty.** A map needs a shape, one
   deploy zone and one expedition. That is it. Build that on your first day, pack
   it, and drive around an empty landscape. Now you have a foundation. People who
   spend three weeks sculpting a canyon and *then* try to make it load spend the
   next three weeks finding out why it does not.

2. **Your map exists in three places at once**, and they drift apart from each
   other constantly. Almost every "I fixed it and nothing changed" story comes
   from editing the wrong copy. [Read that page early](00-start/where-things-live.html).

## Where to start

<ul class="cards">
<li><a href="00-start/what-you-need.html"><strong>What you need</strong><span>The editor, the folders, and roughly how long things take.</span></a></li>
<li><a href="00-start/where-things-live.html"><strong>Where everything lives</strong><span>Three copies of your map, and which one to edit. Read this one early.</span></a></li>
<li><a href="00-start/map-that-loads.html"><strong>Make a map that loads</strong><span>The shortest path from nothing to driving around your own terrain.</span></a></li>
<li><a href="70-shipping/troubleshooting.html"><strong>Something is broken</strong><span>Symptom to cause. Start here when the game misbehaves.</span></a></li>
</ul>

## How this guide marks what it knows

Modding an engine you did not write means some things are documented, some are
discovered, and some are still guesses. This guide labels which is which, on
every claim where it matters.

<p>
<span class="prov prov-doc">documented</span>
Stated in Saber's official guides.
</p>
<p>
<span class="prov prov-schema">schema only</span>
Found in the editor's own type definitions and in the shipped game code, but
missing from the official guides. Real, and usually untested by anyone.
</p>
<p>
<span class="prov prov-unver">unverified</span>
Worked out from evidence but not yet proven in a running game. Test it before you
depend on it.
</p>

Pages still being written are marked in the sidebar. Nothing is padded out with
guesses to look finished.

## What this guide is not

It is not a replacement for the official reference, which remains the place to
look up an exhaustive field list. It is the thing you read first so the reference
makes sense.

It is also not affiliated with Saber Interactive. It is written by people who
build maps, and it includes the mistakes.
