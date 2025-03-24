# 2-Stage Cascode and Single-Gain stage

Most of the underlying points are valid for both the 2-stage cascode and the single-gain stage if not mentioned otherwise.

## Matching and Stability analysis
### Matching
To ensure stable behaviour along the desired frequency range, the rollet stability factor was used.

![alt text](images/stability/s_rollet.jpg)

Some theoretical background can be found inside [the stability.ipynb](common_emitter_amplifier.ipynb) notebook.

### Impedance interdependence
A major issue, especially in the single-gain stage where input and output impedance are strongly correlated, is that matching the input shifts the match at the output.

There are methods to solve this, such as [unilateral gain approach](https://www.mwrf.com/technologies/components/article/21841169/method-simultaneously-matches-inputs-and-outputs). However, this requires the amplifier to be unconditionally stable

### Stability
Matching was attempted in LTSpice. To truly match the components you need to use a multi-port system and the s-parameter characteristics. LTSpice isn't built for this. The match must be physically redone after verification with a VNA.

### LTSpice
To design circuits like this you'd normally need access to software like keysight's ADS software, which has extended support for stability calculation and multi-port system s-parameter modelling. That was only realized after this project, so take the results from the simulation with a grain of salt.

To check out the models, check out the CASCODE_V1-schematic and the GAIN_BLOCK_V1 in [the ltspice-folder](../../simulations/ltspice/version_1/).

The thought-process can be found here [notes.md](../../simulations/ltspice/notes.md) inside the ltspice-simulations folder.


## Phyiscal design
Check out this [README.md](../../kicad/README.md).

## Review
Before production, the images from the [review-folder](../../review/cascode/) were posted to [reddit](https://www.reddit.com/r/PrintedCircuitBoard/comments/1i014uy/rf_pcb_assortment_review/) for review.