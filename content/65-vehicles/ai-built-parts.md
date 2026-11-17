---
title: Building parts with AI
part: Vehicles
order: 671
summary: Bumpers, racks, roof-top tents, fuel cans, recovery boards, axles and winches made with an AI assistant, an image model and Tripo or Meshy. The order that works, and the mistakes that each cost a day or a few hundred credits.
status: draft
---

# Building parts with AI

An AI coding assistant, an image model and a 3D generator such as Tripo or Meshy can between them
make most of what a truck carries: bumpers, roof racks, roll cages, tube fenders, a roof-top tent,
fuel cans, a parts case, recovery boards, a winch, a Dana axle housing. None of them gets it right
by being asked nicely. What follows is the order that works, learned one rejected part at a time.

There are two ways to make a part, and choosing the wrong one is the most expensive mistake:

| The part is | Make it | Because |
|---|---|---|
| tube and plate: a rack, a cage, a bumper frame, sliders, tube fenders | **in code**, from measured centre lines | tube must be round, straight, welded and exactly where the body is. A generator gives you a lumpy approximation of all three |
| a manufactured object: a case, a fuel can, a tent, a winch, an axle housing, recovery boards | **with a 3D generator**, from a real photo | the shape is the whole point, and nobody wants to model a can's ribs by hand |

[Tube parts in code](tube-parts.html) covers the first. This page covers the second, then fitting
either kind to the truck.

## 1. Start from a real object

Every good generated part on this project started from a photo of a real one: a maker's product
shot, an install drawing, or the owner's own truck. Every part made from a description ("a rugged
parts case", "a period-style fuel can") came back looking invented, because it was.

- Find the actual product. Pull several views if the maker shows them.
- If the maker publishes install drawings, use them. One roof rack was rebuilt from the maker's own
  install PDF after a "looks like a rack" version was rejected, and the drawings gave every part.
- Show the photos to whoever the part is for **before** going further. A set of downloaded photos
  is cheap to reject; a set of models is not.

## 2. Make a clean concept from the photo

Generators build from one or a few images, and they build **everything** in the image: the
background, the reflection on the paint, the strap hanging off the side, the logo.

- Cut the object out of the photo with a hand-checked mask. Look at the cut-out at full size, not as
  a thumbnail. A coloured fringe round the edge becomes a coloured rim on the model. One batch of
  eight concepts went to the generator with fringes left in; seven of the eight models were unusable.
- **Paint out every logo and maker's lettering.** A generated model reproduces them, and a published
  mod must not carry someone else's brand.
- Re-light shiny objects with soft, even light first. Reflections turn into false seams: on one
  generated car body the "panel gaps" sat exactly on the reflection bands of the photos.
- A part cut out of a concept sheet (one bumper from a drawing of the whole truck) generates far
  better than a part described in words. Four hand-built versions of one bumper were rejected; the
  first generation from a cut-out of the drawing got the design right.
- Hidden sides get the fewest features that make sense. Every door, step or window you invent on a
  side nobody drew is a guess someone has to catch.
- Get an OK on the concept before spending credits on it.

## 3. Generate

For **Tripo**, the settings that mattered:

- Turn **off** any polygon reduction in the generator. A vehicle generated at a 60,000-polygon cap
  came out with 37 % open edges and 2,199 loose fragments; the same input at 2,000,000 polygons and
  4K texture came out as one piece with 20 open edges. Reduce it yourself afterwards.
- For a whole vehicle, use the multi-view mode (front, back, left, right), with the right view made
  by mirroring the left and flipping its badges back.
- One generation per clean concept. A retry reuses the same input, so a dirty input wastes every retry.

## 4. Clean the model, do not rebuild it

The generated model is the asset. Fix its faults; do not replace it with something you modelled
because it was easier to control. A "cleaned" truck body rebuilt from boxes measured off the
generated one lost everything that made it look right.

- Prove a fault before fixing it: mark it in red on a render and look.
- Common faults: photo background baked into the model, invented backing plates, mask leftovers,
  a hoop generated as a half shell.
- Where a fault is fused into a real part, rebuild **that part only**, on a centre line measured from
  the generated mesh.
- Cut exactly. Split the mesh on the cut line first, then delete. Deleting faces by their centre
  point and filling the hole leaves stepped, spiky edges.
- Weld UV seams before cutting holes in a generated mesh.

## 5. Fit it to the truck

- Scale with **one uniform scale** to a measured feature (the real product's length, a wheelbase,
  the hub centres). A part stretched to fit looks wrong even when every number says it fits.
- Use the part you were given. If someone hands you a model, fit that model. Replacing it with your
  own build because the first fit was awkward throws away their work.
- Rest it on what it sits on. A can on a rack is levelled by its own top and dropped onto the bars,
  not levelled by its base: one generated can had a base plate skewed 2.4 degrees, so every
  base-levelled copy leaned.
- Render it on the truck, **with back-face culling on**, from the angle the player sees, on both sides.

## 6. Into the game

Every mesh the game loads has to pass through the game's own converter, and the game's limits
apply to generated parts like any other:

- **65,534 triangles per mesh.** Two generated parts in one add-on mesh almost always need reducing.
- Normal maps from glTF are green-up; the game reads green-down. Flip the green channel when you
  convert them.
- Each add-on mesh must carry its material, or the game draws nothing and says nothing.
- An add-on needs a slot on the truck and, if it bolts to another add-on, a requirement on that
  add-on. That is its own page: [Add-on slots, dependencies and gear](addon-slots.html).

## What has been checked

Everything above comes from parts that were built, installed and looked at in game, and from the
mistakes along the way. The credit and polygon numbers are from those runs. What is not here yet:
a side-by-side of Tripo against Meshy on the same input, and rigging a generated part to move (a
winch drum, a door).
