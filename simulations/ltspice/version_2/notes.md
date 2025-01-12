# Notes
- V1: Didn't include the transmission-line simulation for the LNA impedance matching
    - V2: Add a transmission line segment, check the S-params and redo the matching
    - 
- Didn't fix the possible stability issues around the amplification-band
    - It seems like changing these values indeed does change the stability
    - It however, does also change the gain.
    - Think about adding an additional base resistor (start with 0 ohm and tweak if necessary)
    - For now leave it the same, make sure to add an extra base-resistor position so you can tweak and check the effects of this base resistor.