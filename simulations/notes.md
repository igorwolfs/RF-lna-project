# Impedances
We'll match both circuits with T-structures on both ends, first end needs to be a T-structure in order to
- Avoid a short to ground through the 5 V power supply (should withtstand 5 V)
- Avoid DC signal from coming through on the antenna side.
- In case a signal needs to be sampled from a higher value, make sure the inductor on the right is isolated.

## Input impedance Z11
183-193j

### Matched with T-circuit
- 1.225 pF
- 21.22 nH
- 3.66 pF (5 V capable)


## Output impedance Z22
7+0.532j

### Matched with T-circuit
- 3.66 pF
- 6.825 nH
- 1.5 pF

# Impedances 2.0
After deciding to add some inductors to block-off the path to the DC supply. The (mostly output) impedance changed significantly, so matching should be redone.

## Input impedance Z11
-> Already matched, input stage impedance is decoupled from output stage / power.


## Output impedance Z22
- 0.85 + 18.2j Ohms

Given an L-match of 4 pF (series), and 20 nH (shunt), we get a positive S22. (about 2.1 dB)

Which means the signal reflected from port 2 is 2.1 dB times the signal going into port 2, so 1.273

### Question: is this a problem?
My initial thought would be it is not, since it is the power reflected from the second port when a signal is incident to it. In reality this is only an issue when there needs to be an "input" in the second line, which there is not.
I would think that as long as the gain is good, there is no real problem.