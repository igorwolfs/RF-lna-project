# Todo
## LTSpice
- Create a PI and T-possible circuit instead of an L-circuit for impedance matching
    - Try to work simply with 2 "series" capacitors and 1 inductor to ground
    - Leave the other one open
    - Best since in case the impedance is larger than thought, we still have space for the necessary decoupling capacitor
- Create a cascode ltspice file in the time-space for input impedance calculations at certain frequencies
- Match using the relevant components

## KiCad
-  Finish the circuit in KiCad
-  Layout the PCB, including 
    - the SMA connectors
    - the power supply
- Add an additional part to the circuit with an antenna 
- Add an additional part with a wideband (low-frequency) rf attenuator

- Think about what other boards you might want to buy / design, since sending costs are also in the high 20-30 euros
    - Maybe some further simple PCB boards without components for RF testing, filters, etc..
    - Frequencies: 0.868, 1.2, 1.5, 2.4 GHz

## OpenEMS
- Simulate the antenna before adding it to the circuit
- Look for an antenna which you can reduce in size (monopole / Meandered inverted-F / Meanderd dipole / Patch)

## Ordering
- Double-check relevant PCB-cut-off

# Download simsmith
https://www.dropbox.com/scl/fo/npviayd3suq8fr7pxx62i/h?rlkey=80ckskojj8e3efs7njtae7ybv&e=1&dl=0
- Input impedance Z11: between 500 (1 GHz) and 250-300 ohms (2 GHz)
- Output impedance Z22: between 60 (0.5 GHz) and 10 ohms (2 GHz)

