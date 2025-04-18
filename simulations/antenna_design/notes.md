# Goal
The goal here is to simulate the basic TI lorawan-antenna example, so that it fits on the board, and do the appropriate 50 ohm impedance matching for it.

# Implement the antenna on the RF-LNA board.
- Create a footprint that looks like the antenna.
- Add a connector on the top side.
- Create the feed-line from the connector towards the antenna.
- Add vias through the antenna.

# Antenna project-FreeCad tips
In the next antenna project, try to make the sheet belong to the same part, and try to have multiple bodies belong to that part.

# Meandering 
When meandering the antenna, the impedance increases because there is
- inductive coupling with meanders (so inductance goes up)

An increased ground plane decreases impedance, since it reduces certain parasitics.

# Stackup
- L1: CU: 0.035 mm
- prepreg: 0.2104 mm prepreg (dielectric 4.4)
- L2: 0.0152 mm copper
- Core: 1.065 mm (dielectric: 4.6)
- L3: 0.0152 mm copper
- Prepreg: 7628, RC 49 %, 0.2104 mm
- L4: CU: 0.035 mm

## Total thickness
thickness = 0.035*2+0.2104*2+0.0152*2+1.065 = 1.5862 mm


## Layers
### L1
0 -> 0.035

### L2
0.2454 -> 0.2606

### L3
1.3256 -> 1.3408

### L4
1.5512 -> 1.5862

## Indicating lengths in freecad
Do indicate the right length in freecad use

1. Select 2-lengths.
2. Length: length in the normal direction compared to main face
3. Length2: length in the direction parallel but opposite to the normal.

So if you want to have an object of length 2 mm, floating 1 mm from the normal then
- length = 3 mm
- length2 = -1 mm

note that for some annoying reason the length2 can't be 0, so we need to use a very small number here instead


## Creating vias in freecad

1. Sketch a single via (hollow cylinder)
2. Open the Draft-tool
3. The "Position" needs to be set to the position where the x, y and z repetition needs to be started from. E.g.: the left/right upper/down most-position.
4. The x/y/z-interval x/y/z needs to be set to the distance between each repetition
5. Use the copy and rotate tool to make multiple copies of the same via-structure and rotate if necessary
6. Make sure to add all of these together inside a single "part"-container
7. Export as STL.


# Gridding issue
Issue: the gridding function is written to ignore closely placed grid elements.

The problem now is that instead of adding part of the vias to the grid, it just sees all the via elements as being placed "too close together", and therefor doesn't add any gridpoints at all.

It seems to get complicated to get an accurate mesh drawn using freecad. Another option is to draw a mesh manually and export it in the python console, import it into freecad and simulate according to that mesh.

## Issues with gridding
I believe the grid created in FreeCad is apparently too narrow, since only the second resonance frequency (around 960 MHz) is recorded. I need to make sure to make this grid narrow enough before starting to simulate.

## Freecad colour selection
- Select copper-Generic for all copper planes and traces

# Antenna impedance-matching
The impedance is expected to be at 868 MHz:
- 146.45290555594192 -2.1068139787461426j
So by matching in simsmith we get the matching circuit:

## Values present on schematic
### Inductors
- 15 nH, 16 nH, 24 nH
### Capacitors
- 1 pF, 3.6 pF, 6.8 pF

## Matching
Make sure to export the S11 values and the impedance values as an s1p-file.
### JLCPCB
Make sure to:
- buy only the matching components which are reused several times
- use larger footprints for the matching components for ease of soldering.