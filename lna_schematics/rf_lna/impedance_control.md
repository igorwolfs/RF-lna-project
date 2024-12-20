# Impedance Control
The stackup for impedance control chosen is the default
- JLC04161H-7628

## PCB Calculator
https://jlcpcb.com/pcb-impedance-calculator
For the following stackup:
- L1: CU: 0.035 mm
- prepreg: 0.2104 mm prepreg
- L2: 0.0152 mm copper
- Core: 1.065 mm
- L3: 0.0152 mm copper
- Prepreg: 7628, RC 49 %, 0.2104 mm
- L4: CU: 0.035 mm

Use a coplanar waveguide.
- Choose a trace width of 0.1 mm
- Can easily handle 0.1635 A, so that's good.
- distance to surrounding ground: 0.2 mm
- Trace width: 0.294 mm
    -> So the total CPW is about 0.7 mm.
    -> We do have enough space however so that should not be an issue.