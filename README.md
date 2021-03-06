# Connecting Rods Inspector – Computer Vision system for the visual inspection of motorcycle connecting rods
<p align="center">
  <img src="https://github.com/bobcorn/connecting-rods/blob/master/demo/gifs/rods.gif">
</p>

Computer Vision system that is able to analyse the dimensions of two different types of connecting rods to allow a vision-guided robot to pick and sort rods based on their type and dimensions.

## Image characteristics
Rods appearing in the images are characterised by the different number of holes: type "A" rods have one hole, whilst type "B" rods have two holes.

### Part 1
We consider that the following simplistic conditions hold for each image:

1. Images contain only connecting rods, which can be of both types and feature significantly diverse dimensions.
2. Connecting rods have been carefully placed within the inspection area so to appear well separated in images (i.e. they do not have any contact point).
3. Images have been taken by the backlighting technique so to render rods easily distinguishable (i.e. much darker) from background. However, for flexibility reasons the system should not require any change to work properly with lighting sources of different power.

### Part 2
We no longer consider the simplistic conditions holding for the previous part:

1. Images may contain other objects (i.e. screws and washers) that need not to be analysed by the system.
2. Rods can have contact points but do not overlap one to another.
3. The inspection area may be dirty due to the presence of scattered iron powder.

## Functional specifications
### Part 1
For each connecting rod appearing in each image, the vision system must provide the following information:

1. Type of rod (A or B).
2. Position and orientation (modulo π).
3. Length (L), Width (W), Width at the barycenter (WB).
4. For each hole, position of the centre and diameter size.

### Part 2
For each image, the following requirements must be met:

1. Distracting objects must be ignored.
2. Touching rods must be recognised separately.
3. Iron powder presence must be managed as to not interfere with the analysis.

## Performances
Performances are calculated as the average observed FPS of 10 000 consecutive software executions on a Intel Core i5 Dual-Core 2,7 GHz processor.

* 33 FPS

## Full demo

<p align="center">
  <img src="https://github.com/bobcorn/connecting-rods/blob/master/demo/gifs/full.gif">
</p>

## Requirements
The following Python packages must be installed in order to run the software:

* numpy
* opencv-python
* scipy

## Usage
Simply run the "main.py" script from terminal, after making sure it is located in the same directory of the "images" folder:

```bash
python main.py
```

or:

```bash
python3 main.py
```
