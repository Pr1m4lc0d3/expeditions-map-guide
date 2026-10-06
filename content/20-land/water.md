---
title: Rivers, lakes and waterfalls
part: The land
order: 240
status: draft
summary: Give water somewhere to go, hide the edges, and keep the result editable whether you build it yourself or with AI.
---

A river is not a blue road. Putting a strip of water across a valley does not make
that strip fit the valley. It gives you a water surface. The ground still has to
provide the bed and the banks.

Get those three things to agree first. Foam can wait.

## The mistake that looks wrong immediately

If you can see straight, square or saw-toothed edges floating over the ground,
you are seeing the edge of the water object instead of a shoreline.

The fix is not always more width, and it is not always less height. Measure both.
The visible water should meet soil on each side, with the outer mesh edges hidden
inside the banks. Check from road height, not only from directly above.

## Measure in two directions

**Along the channel**, measure the bed and the fall toward the outlet. A flowing
reach needs a connected downhill route. Do not stretch one horizontal sheet down
a steep ravine. Equally, do not force a pool to follow every bump in its bed.

**Across the channel**, measure from bank to bank, at right angles to the local
flow direction. The water surface is normally level across a section. Follow the
bend when choosing that direction; the map's X axis is not the river's cross-section.

A heightmap is a starting point, not a promise about underwater ground. Its survey
and processing may describe a water surface rather than the actual bed. Inspect
what your particular dataset contains before designing a lake around it.

!!! warning "The road may not be the raw terrain"
    Road flattening can change the surface you drive on. Do not turn it off just
    to make a puddle show. You may uncover a much deeper hollow than intended.

## Give each piece a name

You should not have to click seventy objects to find one crossing.

Our convention is `W00_R000_Name_ReachDescription`. `W00` identifies a channel;
`R000`, `R001` and `R002` run downstream within it. Tributaries get their own channel
codes and a recorded connection to the receiving reach. Lakes use `L000`, road
pools `P000`, and culverts `C000`.

Use the real drainage name when you can verify it against mapping of that actual
channel. Otherwise use a clearly descriptive name such as
`W01_R000_UnnamedDrainage_UpperChannel`. A named canyon nearby is not evidence that
its stream has the same official name.

The label is for people. The object ID is for the files. Keep both, and keep a
small index linking labels, IDs, source files and upstream/downstream neighbours.

!!! warning "A name in a spreadsheet is not a name in the editor"
    Confirm that the editor displays your label and lets you select its nodes.
    If individual rivers cannot retain labels, test a named group containing one
    river. Save and reopen it before adopting the method. The exact serialization
    is still unverified in this workflow; do not invent a River XML attribute.

## Build the first reach by hand

1. Back up a map that already rebuilds and deploys. Work on a separate copy.
2. Choose a short, uncomplicated channel. Measure its bed and both banks.
3. Use **Add River** from the terrain's context menu, then position its nodes along
   the channel. Adjust node height and width together.
4. Rebuild and inspect the whole reach from both banks. Check between nodes and
   around bends, not just where the handles sit. Lower, narrow, widen or reroute
   where needed. If no banks exist, design the channel before adding more water.
5. Inspect both ends. Connect them to another reach, a pool or a deliberately
   concealed endpoint. Do not leave a visible square cap.
6. Give the reach its label and test that you can find its nodes after reopening.
7. Pack and drive it. Then extend it.

The editor provides river nodes and separate water painting controls.
<span class="prov prov-doc">documented</span> See
[Saber's river instructions](https://expeditions-guides.saber.games/map_modding/creating_a_map/rivers_and_water_objects/adding_rivers_and_water_objects/)
for the controls in your editor version.

## A lake is a bowl, not a wide river

Pick a water elevation and inspect the entire shoreline. The surrounding terrain
must contain that level. A low saddle is an outlet, not a bank you can ignore.
Use level water nodes, shape the water object to cover the basin, and hide its
outside edges under surrounding terrain. Check the bed depth separately from the
surface height, especially anywhere a truck can enter.

## When the channel goes under a road

Mark a planned culvert explicitly. Do not let an automatic watershed tool treat
the road embankment as the end of the channel.

For a crossing designed with matching mouth levels, connect water on both sides
at that specified elevation, beneath the roadway. Keep the exposed inlet and
outlet contained by banks. The covered section is allowed to disappear into the
road terrain; raising it to become visible would defeat the crossing.

The culvert model and its opening still need placement and collision checks.
Drawing water through solid ground does not cut a tunnel. A ford or washout is a
different design, not an excuse to apply this exception everywhere.

## Make it move after it fits

Flow direction, speed and foam are not the same setting. Neither are brown water,
wet ground and deep mud. Check each one independently. Use the editor's water
brushes and verify a small painted sample before asking a script to write masks.

Put foam where water is disturbed, then carry it downstream. Perfect matching
white bands on both banks tend to look painted on. Treat falls as separate drops
with a receiving pool and suitable effects, not a stretched river ribbon. The
repeatable waterfall procedure is still being tested.

## Ask AI for measurements, not reassurance

A useful request looks like this:

> Survey this channel along its bed and across both banks. Name every reach,
> preserve my edits, and show where the proposed water has no enclosing bank.
> Export one short test reach only. Do not change the road. Mark this crossing
> as a planned culvert with matching mouth levels.

Ask for the measurements, a connectivity index, a change list and a rollback
copy. Then inspect the result yourself. A script passing its tests is not the
same as the editor rebuilding, and neither proves the packed map deploys.

The current **expeditions-waterways** skill is a workflow preview for Claude Code
and Codex. It is not yet an automatic river designer. One short Shafer Trail
Monsoon reach has received a positive visual review; bends, junctions, naming
serialization and full-network export still need validation.

!!! tip "Keep the change small enough to blame"
    Build one reach. Check it. Save a known-good version. Add the next reach.
    If a build fails, undo that last isolated change before collecting more
    guesses. A crash at a step labelled plants does not, by itself, prove that
    the plants caused it.
