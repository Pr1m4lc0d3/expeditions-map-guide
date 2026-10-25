---
title: Using real-world terrain
part: The land
order: 250
status: draft
summary: Importing real elevation data, and the surprising amount of design work it does for you.
---

You do not have to invent your landscape. Public survey data gives you the height
of real ground, and a real place has already solved problems that are hard to
solve by hand: where the valleys drain, how steep the slopes sit, and where a road
can climb a hillside.

This page covers where that data comes from, what it does and does not contain,
and the checks that catch the mistakes it makes easy.

## Where the data comes from

| source | coverage | resolution | notes |
|---|---|---|---|
| **USGS 3DEP** | United States | `1 m` | bare-earth lidar, no API key. Best by far |
| global terrain tiles (AWS terrarium set) | worldwide | roughly `10` to `30 m` | too coarse for roads to show up |

<span class="prov prov-unver">measured</span>

**Bare-earth** means the survey has had trees and buildings removed, leaving the
ground itself. At `1 m` that is finer than the map's own height grid, which on a
full-size map is `0.5 m` per sample in the built terrain and `2 m` per sample in
the import file.

The 3DEP service refuses very large requests, so a full map is fetched in
pieces of about `2000` pixels each and stitched.
<span class="prov prov-unver">measured</span>

### Fetching it with the toolkit

`fetch_terrain.py` fetches 3DEP for a point, crops it to the map's size and
writes the import file at the size the editor expects. It also reports the Max
height to use and the height step that results.

```
python fetch_terrain.py <lat> <lon> --span 2016 --blocks 84
python fetch_terrain.py <lat> <lon> --span 2016 --blocks 84 --level level_<name> --apply
```

Then open the map in the editor and use **Copy Source Heightmap** to import it.
Read [how terrain works](terrain.html) first: the import replaces the whole
terrain, and a baked terrain file left from a copied map will hide the result.

Outside the United States the toolkit's `expeditions/dem.py` uses the global
tiles instead. That route has not been tested on a map in this guide.

### Precision follows real elevation

The height format's smallest step grows with height above zero, not with the
map's relief. A map whose ground sits at `1,600` to `1,977 m` above sea level
would be stored with far coarser steps than a valley near sea level if those
heights were kept as they are.
**Lower the floor** so the lowest point of the map sits near zero. That is what
buys precision. <span class="prov prov-unver">measured</span>

## Real terrain already contains its roads

A road is a physical thing: a cut-and-fill bench in the hillside. Bare-earth
lidar measures the ground, so it measures the road as part of it.

That means **the road's design comes with the data.** Its gradient, where the
switchbacks go and how deep it cuts were solved on the ground by whoever built
it. You do not need to invent an alignment for a real place.

It was checked on the Moki Dugway in Utah, by looking only at the elevation for
flat ribbons hemmed in by steep ground (slope under `10` degrees, with more than
`20 m` of relief within `41 m`): <span class="prov prov-unver">measured</span>

| found from elevation alone | documented |
|---|---|
| about `4,065 m` of road | `4,800 m` (3 miles) |
| benches spanning `311 m` of climb | `366 m` (1,200 ft) |

Both within about 15%.

!!! warning "The terrain contains the road, but cannot say which bench it is"
    The same test on a canyon road in Canyonlands, Utah, reported `23,518 m` of road
    against `7,193 m` actually mapped, three times too much. Canyonlands *is*
    benches: mesa tops and rim ledges are natural flat ground between cliffs,
    and they pass the test perfectly. <span class="prov prov-unver">measured</span>

    On benched or mesa country, take the route from mapped road data and use the
    elevation only for height. Detecting benches is a way to find candidates,
    not a way to route.

Road centre lines as lines on a map are available from OpenStreetMap or the US
National Map. The toolkit's `fetch_trails.py` pulls tracks from OpenStreetMap and
lays them as [overlays](roads.html), with Flatten on and ApplyOffset off. The
line comes from the mapping, and the height comes from the terrain, because an
overlay has no height of its own.

```
python fetch_trails.py level_<name> <lat> <lon> --span 2016
python fetch_trails.py level_<name> <lat> <lon> --span 2016 --apply
```

## Getting the orientation right

It is easy to import a real place mirror-imaged, and hard to notice. A valley
looks like a valley either way round. What gives it away is that two layers built
from the same place stop agreeing: the roads no longer sit on the benches in the
ground.

That exact failure happened. The terrain fetch skipped the step that turns a
north-up survey image into the map's frame, while the road fetch applied it, so
terrain and roads were mirror images of each other. Every check on the map passed,
because **each check looked at one layer on its own**. A check of one layer cannot
see a disagreement *between* layers. <span class="prov prov-unver">measured</span>

The check that caught it scores how many road points land on benches found in the
terrain:

| reading | road points on a bench |
|---|---|
| chance | `14.7%` |
| broken map, as built | `10.6%`, worse than chance |
| broken map, flipped east to west | `53.5%` |
| after the fix, as built | `53.7%` |

<span class="prov prov-unver">measured</span>

So: after importing a real place, **overlay the roads on the terrain and confirm
they agree.** In the toolkit:

```
python check_new_map.py <name> --relief <metres>
```

It takes the map name without the `level_` prefix and the relief reported by the
fetch.

!!! warning "Do not trust a compass guess"
    Work out which way round a map is from evidence, such as where a change you
    made shows up in the files, never from an assumption like "west is on the
    left". On one map, the side that had just been edited was at the high-x end,
    the opposite of the obvious guess. <span class="prov prov-unver">measured</span>

## Water is never in the elevation data

The survey gives you the valley, the banks and the full cross-section. It does
not give you a riverbed or a lake bed.

- USGS **hydro-flattening** levels every body of water of `0.8 ha` (2 acres) or
  more to a flat, level surface, by specification.
- The infrared lidar used does not see through water anyway.

On the Buffalo River in Arkansas, the valley came through `142 m` deep with both
bluffs. The water surface varied by `0.092 m` across a `35 x 36 m` patch: a
plane, not a channel. <span class="prov prov-unver">measured</span>

For the water's *course*, the US **National Hydrography Dataset (NHD)** gives
stream centre lines, flow direction, connections and lake outlines, which is what
a river object needs. It gives no depth.

For the *bed*, sources exist but cover only some waters:

- USGS inland bathymetry, for selected lakes, rivers and reservoirs
- existing combined land-and-water surveys for a few large lakes, including Lake
  Powell, Lake Tahoe and Crater Lake
- US Army Corps of Engineers sonar surveys
- state natural resource departments, several of which publish lake depth data
- for a reservoir, maps made before the dam. The drowned valley floor is the bed

None of these has been imported into a map in this guide yet. See [rivers, lakes
and waterfalls](water.html) for building the water itself.

## Matching the colour of a real place

Satellite imagery providers disagree with each other, a lot, about colour. Over
one desert map, four sources gave: <span class="prov prov-unver">measured</span>

| source | hue | reads as |
|---|---|---|
| Google satellite | `11` to `19` | dusty pink |
| ground photographs (Street View) | `60` to `75` | tan |
| USGS NAIP aerial, `1 m` | `72` to `78` | warm tan |
| Esri World Imagery | about `90` | olive tan |

The ground was painted to match the first source and came out about 60 degrees
of hue too pink. Two independent sources, the aerial survey and the ground
photographs, agreed with each other; the provider the map was matched to was the
odd one out.

**One imagery source is not a reference.** Compare several from separate
pipelines, and include photographs taken on the ground.

Lightness and saturation were already right on that map; only the hue was off.
The corrected textures were confirmed in the game files but have not yet been
checked by eye in the editor. More on this in [colour and
textures](../30-dressing/colour.html).

## Not yet known

- The global terrain route outside the United States has not been used for a map
  here.
- No bed data has been imported for a lake or river yet.
- Whether the colour correction above looks right in the editor and in game.
- Whether a map with Max height above `512` works.

Read Saber's pages on terrain first:

```
python wiki.py howto terrain
```
