# Todo
## LTSpice
- Create a PI and T-possible circuit instead of an L-circuit for impedance matching
    - Try to work simply with 2 "series" capacitors and 1 inductor to ground
    - Leave the other one open
    - Best since in case the impedance is larger than thought, we still have space for the necessary decoupling capacitor
- Create a cascode ltspice file in the time-space for input impedance calculations at certain frequencies
- Match using the relevant components

-> NOTE: we redid some of the stuff here due to adding of inductors
- It changed the required matching impedance
- It made sure the signal didn't travel up to the source


## KiCad
### CASCODE 2-stage amplifier
-  Finish the circuit in KiCad
-  Layout the PCB, including 
    - the SMA connectors
    - the power supply (choose a separate connector here)


### Single-transistor amplifier
- Add an additional part with the same transistor, and a single-ended


### Antenna design 


### Test-trace design

- Think about what other boards you might want to buy / design, since sending costs are also in the high 20-30 euros
    - Maybe some further simple PCB boards without components for RF testing, filters, etc..
    - Frequencies: 0.868, 1.2, 1.5, 2.4 GHz


## OpenEMS
- Simulate the antenna before adding it to the circuit
- Look for an antenna which you can reduce in size (monopole / Meandered inverted-F / Meanderd dipole / Patch)


## Ordering
- Double-check relevant PCB-cut-off


## Testing
- Add a bandpass filter
- Heat-sink? Is it even necessary assuming we'll get a current of < 100 mA
- RF power meter


### Resources
- Blog for testing afterwards: https://nuclearrambo.com/wordpress/designing-and-testing-a-low-noise-amplifier-part-1/