---
title: Small RC drones
part: Vehicles
order: 670
summary: How a drone the size of an RC car was made to deploy, drive and ride over mud without digging trenches. Lighter weight doesn't fix the ruts; four fixed-size numbers in the game do.
status: draft
---

# Small RC drones

**Works, on PC, with a patched game.** A drone about half the size of the stock scout drone, built
to look like an RC crawler, deploys from a truck, drives, and rides over real mud without leaving a
rut. That's confirmed in game (2026-11-22). It needs two changes to the game files themselves, so a
mod on mod.io can't deliver it alone, and consoles can't run it. The tools that apply the changes
aren't released yet.

Four separate things stopped it, and each one looked like the others from the driver's seat. They
are below in the order they were found.

## 1. The game didn't recognise a mod drone

A carried drone is two classes. The drone itself is a truck class with `IsWheelDrone="true"`. The
part that carries it is an add-on with `HasWheelDrone="true"` and `WheelDroneType="<the drone's
class name>"`.

The game decides what kind of drone it has **by name**. A script in `initial.pak` compares the name
with exactly `drone_anchor`, `drone_cargo` and `drone_scout`. A class shipped in a mod loads under
its own name plus the mod's id (`my_drone` becomes `my_drone_1234567`), so it never matches. The
drone is typed "none", it won't deploy, and the garage throws script errors. Renaming the class to
`drone_scout` doesn't help, because the id is still added.

**The fix** is a two-byte change to that script, so any non-empty drone name counts as a scout. An
earlier version compared with a name nothing uses. That also made every ordinary add-on count as a
scout, and it filled the inventory bar with dozens of scout-drone tabs. Comparing with the empty
string fixed that.

## 2. The wheels never turned

With the type fixed, the drone deployed and sat there. The wheels didn't turn at any torque.

The cause was found by bisection: take the stock scout drone, which drives, change **one** thing
from the custom drone, and see which copy stops. Only one did. The custom drone's wheel block said
`Torque="full"` where the stock drone says `Torque="default"`. On a drone, `full` means the wheels
never get power. Every other difference (axles, mesh, engine, gearbox, suspension, tyre class) was
harmless.

## 3. Scale the stock drone, don't invent one

The settings that work all come from scaling the stock scout drone class by one factor *k* (0.5 for
half size):

| Setting | Scaled by |
|---|---|
| positions (`Pos`, `Origin`, `CenterOfMassOffset`), `SteeringJointOffset`, wheel `Scale` and `OffsetZ` | *k* |
| body and tyre mass | *k*³ |
| engine torque | *k*⁴ |
| gearbox `AngVel` | 1 / *k* |
| suspension `Height`, `SuspensionMin`, `SuspensionMax` | *k* |
| suspension `Strength` | *k*² |

Keep the body's collision box about 6 cm above the tops of the tyres, or it grabs the tyres. Then
put any body you like on top as the drawn mesh.

## 4. The ruts, and why less weight doesn't fix them

The drone now drove, but on dirt, grass and mud it dug itself a trench and sank, while a truck
beside it left no mark.

**Making it lighter doesn't help.** Here's what was tried:

- weight from 1/8 down to 1/64 of the scaled value
- stiffer springs
- wider tyres, firmer tyres
- tyre `PushUpFactor` up to 10,000
- turning off the wheel-track stamp

Every version still dug in. The very light ones bounced or flew off the ground on deploy and broke
their engines landing. `PushUpFactor` only acts in water.

The reason is in the game's ground code, read from `Expeditions.exe`. Three amounts are fixed sizes
built for trucks. A small toy and a 10-tonne truck get the same:

- **Mud sink.** A tyre sinks half the painted mud's thickness before the mud starts holding it up.
  That's a few centimetres for any truck, and most of a small tyre.
- **Ground digging.** Each contact on soft ground can lower the ground under the tyre by up to
  15.6 cm.
- **The rut stamp.** The mark pressed into mud is never smaller than 0.3 m wide and 0.4 m in radius,
  however small the tyre. On normal soil there's often a thin layer of mud you can't see, so this
  fires even where the ground looks dry.

None of these reads the vehicle's weight or the tyre's size, so no setting in a class file reaches
them.

**The fix** is four small patches to `Expeditions.exe`. They act only on tyres under 0.33 m in radius
(the stock drone's tyre). Every truck and stock drone runs exactly as before.

1. The mud sink shrinks with the tyre, by (radius ÷ 0.33)⁴.
2. Small tyres never lower the ground layer.
3. Small tyres get full mud support at a quarter of the sink, so they ride on thin mud.
4. The rut stamp is drawn at the tyre's own size.

With all four in, the drone drove a whole map without digging a rut and crossed real mud like a
real RC car.

## What's still open

- A game update or an Epic "verify files" restores the original `Expeditions.exe` and `initial.pak`.
  The patches have to go back on after each one.
- The drone shakes slightly when it sits still with the motor running.
- The patch tools aren't public yet. This page will link them when they are.
