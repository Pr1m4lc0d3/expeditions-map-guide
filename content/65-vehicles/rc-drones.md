---
title: Small RC drones
part: Vehicles
order: 670
summary: How to make a drone the size of an RC car that deploys from a truck, drives, and rides over mud without digging itself in. Four steps, two of them changes to the game files.
status: draft
---

# Small RC drones

**Works, on PC, with a patched game.** A drone about half the size of the stock scout drone, built
to look like an RC crawler, deploys from a truck, drives, and rides over real mud without leaving a
rut. That's confirmed in game (2026-11-22). Two of the steps change the game's own files, so a mod
on mod.io can't deliver it alone, and consoles can't run it. The tools that apply those changes
aren't released yet.

A carried drone is two classes. The drone is a truck class with `IsWheelDrone="true"`. The part
that carries it is an add-on with `HasWheelDrone="true"` and `WheelDroneType="<the drone's class
name>"`. Build both, then work through the four steps below.

## 1. Let the game accept a drone from a mod

The game decides what kind of drone it has **by name**. A script in `initial.pak` compares the name
with exactly `drone_anchor`, `drone_cargo` and `drone_scout`. A class shipped in a mod loads under
its own name plus the mod's id (`my_drone` becomes `my_drone_1234567`), so it never matches. The
drone is typed "none", it won't deploy, and the garage throws script errors. Renaming your class to
`drone_scout` doesn't help, because the id is still added.

**Do this:** change that comparison so any non-empty drone name counts as a scout. It's a two-byte
change to the script in `initial.pak`. Compare with the empty string, not with a name nothing uses.
The second version also makes every ordinary add-on count as a scout, and the inventory bar fills
with dozens of scout-drone tabs.

## 2. Use the stock drone's wheel settings

In the drone's wheel block, use `Torque="default"`, as the stock drones do. With `Torque="full"` the
drone deploys and sits there, and the wheels never turn at any engine torque.

If a drone won't drive and you can't see why, bisect it. Copy the stock scout drone, which drives,
change one thing from your drone, and test. The copy that stops driving names the cause.

## 3. Scale the stock drone, don't invent one

Start from the stock scout drone class and scale it by one factor *k* (0.5 for half size):

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

## 4. Stop the ruts

At this point the drone drives, but on dirt, grass and mud it digs a trench and sinks. The cause is
in `Expeditions.exe`. Three amounts in the game's ground code are fixed sizes made for trucks, and
nothing in a class file reaches them:

- **Mud sink.** A tyre sinks half the painted mud's thickness before the mud starts holding it up.
  That's a few centimetres for any truck, and most of a small tyre.
- **Ground digging.** Each contact on soft ground can lower the ground under the tyre by up to
  15.6 cm.
- **The rut stamp.** The mark pressed into mud is never smaller than 0.3 m wide and 0.4 m in radius,
  however small the tyre. Normal soil often carries a thin layer of mud you can't see, so this fires
  even where the ground looks dry.

**Do this:** four small patches to `Expeditions.exe` that scale those amounts to the tyre. They act
only on tyres under 0.33 m in radius (the stock drone's tyre), so every truck and stock drone runs
exactly as before.

1. The mud sink shrinks with the tyre, by (radius ÷ 0.33)⁴.
2. Small tyres never lower the ground layer.
3. Small tyres get full mud support at a quarter of the sink, so they ride on thin mud.
4. The rut stamp is drawn at the tyre's own size.

With all four in, the drone drives a whole map without digging a rut and crosses real mud like a
real RC car.

## What's still open

- A game update or an Epic "verify files" restores the original `Expeditions.exe` and `initial.pak`.
  The patches have to go back on after each one.
- The drone shakes slightly when it sits still with the motor running.
- The patch tools aren't public yet. This page will link them when they are.
