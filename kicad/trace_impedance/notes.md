# Notes on impedance matching
It is apparent that when there's too much distance between the GND and trace layer, the trace must become too wide to achieve matching.

So remove the gnd layer 4 and 3 below the antenna, and keep the gnd plane at 2. Stitch this gnd plane together with the antenna.

IMPORTANT; only JLC04161H-3313 works with economic PCBA. Trace length there is different, thus use this trace
