# KiCad Schematics

## Cascode and Single-Gain Stage
### Input voltage
Assume a max input voltage of 1 mV (close to the transceiver) at 868 MHz.
Given a gain of 25 dB.

### Current variation
Current amplitude is somewhere between 18.4 -> 25.6 mA at the oscillation frequency (which is pretty huge).

So required charge over half a period is (25.6-18.4) * (T/2) =  (25.6-18.4)e-3/ (868e6 * 2) = 4.15 pC

Make sure the capacitor arrays carry at least that amount of charge at 5 V.
So 4.15 pC / 5 V < 1 pF, so the capacitor needs to be at least 1 pF (easy).

### Supply voltage
Pick 5 V supply voltage with component L78L05 (cheap, basic component).

Add LED to verify power ON.

### Capacitors
Capacitor Q-factor: capacitor's reactance / capacitor's parasitic resistance.
- The bigger Q, the smaller the ESR relative to the reactance, the better.

### Inductors
Finding a good AC blocking inductor that is
- About 100 nH
- Self resonant-frequency beyond 2 GHz
Seems to be quite the task


### Resistor size
- Always choose smallest package with relevant power rating, to minimize parasitics.
- Probably good up to a few GHz, once going above 2 GHz make sure to get specialized once.


### Thermal relieves
To make soldering the matching components easier, use thermal relieves.

## Antenna

### Design
#### Matching circuit
Estimated using [SimNec](https://www.ae6ty.com/smith_charts/) and [OpenEMS](https://www.openems.de/).

#### CPW to antenna transition
Non-ideal, was a guess based on a quick search for ideal impedance transition methods.

### Simulations
Simulation data for the antenna can be found inside the [rf-simulations repo](https://github.com/igorwolfs/RF-simulations/tree/main/rf_simulations/lorawan_meandered_monopole).

### Verification
Initial verification results using a NanoVNA show similar results to the OpenEMS simulation.

## JLCPCB Stackup
The jlcpcb-[trace impedance calculator](https://jlcpcb.com/pcb-impedance-calculator
) tool was used for trace thickness calculations for our coplanar waveguide. Stackup: JLC04161H-3313 (economic PCBA).

For the following stackup:
- L1: CU: 0.035 mm
- prepreg: 0.2104 mm prepreg
- L2: 0.0152 mm copper
- Core: 1.065 mm
- L3: 0.0152 mm copper
- Prepreg: 7628, RC 49 %, 0.2104 mm
- L4: CU: 0.035 mm

Use a coplanar waveguide.
- distance to surrounding ground: 0.3 mm
- Trace width: 0.3244 mm
    -> So the total CPW is about 0.3244+0.6 = 0.9244 mm.
    -> We do have enough space however so that should not be an issue.

Note: to much distance between GND and trace requires the trace to become wider.

## Checks before ordering
- Component check: 
    - Do all components have the expected value
    - Do all components have the expected footprint size
- Gerber check:
    - Are the groundplanes adequately removed, is there ground plane where there needs to be.
    - Are the components connected as they are supposed to?