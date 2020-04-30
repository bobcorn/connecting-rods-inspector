# Visual Inspection of Motorcycle Connecting Rods
<p align="center">
  <img src="https://github.com/bobcorn/connecting-rods/blob/master/demo/gifs/rods.gif">
</p>

Computer vision system for visual inspection of motorcycle connecting rods. The system is able to analyse the dimensions of two different types of connecting rods to allow a vision-guided robot to pick and sort rods based on their type and dimensions. The two rod types are characterized by a different number of holes: Type A rods have one hole whilst Type B rods have two holes.

## Image characteristics
### Part 1
For this part, we consider that the following simplistic conditions hold for every image:

1. Images contain only connecting rods, which can be of both types and feature significantly diverse dimensions.
2. Connecting rods have been carefully placed within the inspection area so to appear well separated in images (i.e. they do not have any contact point).
3. Images have been taken by the backlighting technique so to render rods easily distinguishable (i.e. much darker) from background. However, for flexibility reasons the system should not require any change to work properly with lighting sources of different power.

### Part 2
For this part, we no longer consider the simplistic conditions holding for Part 1:

1. Images may contain other objects (i.e. screws and washers) that need not to be analysed by the system.
2. Rods can have contact points but do not overlap one to another.
3. The inspection area may be dirty due to the presence of scattered iron powder.

## Functional specifications
For each connecting rod appearing in the image, the vision system must provide the following information.

### Part 1
1. Type of rod (A or B).
2. Position and orientation (modulo π).
3. Length (L), Width (W), Width at the barycenter (WB).
4. For each hole, position of the centre and diameter size.

### Part 2
1. Distracting objects must be ignored.
2. Touching connecting rods must be recognised separately.
3. Iron powder presence must be managed as to not interfere with the analysis.

## Benchmarks
33 FPS (on average)

## Full demo

<p align="center">
  <img src="https://github.com/bobcorn/connecting-rods/blob/master/demo/gifs/full.gif">
</p>

## Usage

Simply run the "main.py" script from terminal (making sure it is located in the same directory as the "images" folder):

```bash
python main.py
```

or:

```bash
python3 main.py
```
