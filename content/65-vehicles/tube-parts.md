---
title: Tube parts in code
part: Vehicles
order: 672
summary: Roof racks, roll cages, bumpers and tube fenders written as code from measured centre lines, with an AI assistant doing the writing. What to ask before drawing anything, and the checks that catch gaps, inside-out tubes and floating ends before anyone sees them.
status: draft
---

# Tube parts in code

A roof rack is a few dozen tubes. Each one is a centre line, a radius, and two ends that land on
something. Written as code (a list of points, bent with true arcs, swept into a tube), the rack
comes out exact, symmetric and adjustable: move one number and the whole rack follows. An AI
assistant can write that code well. It can also produce, very confidently, a rack whose legs stop
in mid-air, whose tubes are inside out, and that looks nothing like what was asked for. Everything
on this page is a guard against one of those.

## Ask before drawing

Nearly every rejected tube part on this project was a guess that should have been a question. Ask
these, in one message, before any geometry:

1. **Reference**: a photo, an install drawing, or a sketch on the truck.
2. **What each end lands on**: a bumper top, the frame, a hinge, another tube.
3. **Body cut**: none unless asked. A fender flare sits on the panel; the panel is cut only for tyre room.
4. **What it must clear**: tyres at full steer, the hardtop, the tailgate, other add-ons.
5. **Dimensions, angles and body lines** it should follow.
6. **Finish**: paint, bare, chrome caps.
7. **Game fit**: which slot, what it carries, what it requires.

Read sketches from a **gridded side view** (an orthographic render with a metre grid) and say the
points back before building: "the lower rail runs from x -0.95 to the rear leg at 1.57 m, dropping
6 cm". A sketch read by eye from a perspective screenshot gets the slope and the end points wrong.

Build what was drawn and nothing else. Extra trusses, gussets and brackets the sketch did not show
read as clutter, not care: one side frame went through four rounds because each version added steel
nobody had asked for.

## The geometry rules

- **Centre to centre.** A tube that meets another tube ends on the other's centre line, not on its
  surface. Nothing is cut off in mid-air.
- **Bends are true arcs** with a real bend radius, and the tube's rings are dense in the bend (one
  every few degrees) with a frame that does not twist. Otherwise elbows come out faceted.
- **A tube ending on a flat surface is pushed past it** far enough that its whole square-cut rim is
  buried (radius x tan(lean), plus a few millimetres). A leaning leg stopped exactly at the plate
  leaves a wedge of daylight under its high side.
- **Weld beads follow the real joint.** A bead is a small tube laid along the line where one tube's
  surface meets the other's. A plain ring square to the tube floats off one side whenever two tubes
  meet at an angle; trace the intersection instead.
- **Feet are plain squared plates** sitting flat on a real horizontal surface. No brackets unless asked.
- **Follow the body's lines.** A leg that runs parallel to the body's own corner, a side rail that
  carries the line of the cab: that is what makes a part look like it belongs to the truck.

## Faces must point out

The game draws only the side of a face that points toward the camera. A tube swept with its faces
pointing **inward** looks almost right in most renders and shows its inside in game. This shipped
once and was caught by the owner, not by a render, because the renderer drew both sides.

- Measure the winding of every generated piece before it goes near the game: the signed volume of a
  closed piece, or the share of a tube's faces pointing away from its axis.
- Render with **back-face culling on**.

## Check it before anyone else does

Before sending a render, run the self-check on every joint:

- close-ups of each joint from behind and from three-quarter, both sides of the truck;
- no tube end in the air, no gap at a foot, no bead floating off a tube;
- clearances measured, not eyeballed ("11.7 cm to the hardtop", not "looks clear");
- triangle count under the game's 65,534 per mesh.

## Where to find working code

The truck-building code these rules came from is not public yet. Until it is, ask an assistant for
the methods by name: arc fillets between straight runs, a rotation-minimising frame for the sweep,
buried tube ends, beads traced on the intersection, faces flipped outward by signed volume.

## What has been checked

Racks, a roll cage, rear legs landing on a bumper, tube fenders and a side frame with recovery
boards were built this way and checked in game. The rules above each came from a fault that
reached a render or the game first.
