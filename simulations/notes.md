# LNA
## Stability
Check Rollet stability criterion and others:
 ( 1-POW(S11(v1),2)- POW(S22(v1),2)  + POW(S12(v1)*S21(v1),2)) / (2*abs(S12(v1)) * abs(S21(v1)) )
## Impedances
We'll match both circuits with T-structures on both ends, first end needs to be a T-structure in order to
- Avoid a short to ground through the 5 V power supply (should withtstand 5 V)
- Avoid DC signal from coming through on the antenna side.
- In case a signal needs to be sampled from a higher value, make sure the inductor on the right is isolated.

### Input impedance Z11
183-193j

### Matched with T-circuit
- 1.225 pF
- 21.22 nH
- 3.66 pF (5 V capable)


### Output impedance Z22
7+0.532j

### Matched with T-circuit
- 3.66 pF
- 6.825 nH
- 1.5 pF

## Impedances 2.0
After deciding to add some inductors to block-off the path to the DC supply. The (mostly output) impedance changed significantly, so matching should be redone.

### Input impedance Z11
-> Already matched, input stage impedance is decoupled from output stage / power.


### Output impedance Z22
- 0.85 + 18.2j Ohms

For some weird reason, the output impedance became inductive, and hard to match.

Given an L-match of 4 pF (series), and 20 nH (shunt), we get a positive S22. (about 2.1 dB)

Which means the signal reflected from port 2 is 2.1 dB times the signal going into port 2, so 1.273

### Matching to 50 Ohms
When matching the impedance to 50 ohms using an CL-circuit (4pF, 20nH), we get a 50-ohms but phase-shifted impedance, which obviously isn't what we want.


### Question: is this a problem?
My initial thought would be it is not, since it is the power reflected from the second port when a signal is incident to it. In reality this is only an issue when there needs to be an "input" in the second line, which there is not.
I would think that as long as the gain is good, there is no real problem.

However power reflected at port 2 might cause oscillations and also makes it hard to match with caps in series since the goal in this case is to decrease impedance.
Since impedance here is too low, we need to add an inductor first to increase the impedance at that frequency, and then make it resonate with the capacitor to get a real impedance of 50 ohms.

### Question: what caused the output impedance to become so inductive?
It seems like the reason for the impedance to become inductive is the inductance at the top cascode transistor collector which is meant to decouple the impedance.
Removing this inductance while keeping all other inductances intact leads to an impedance of:
- 5.17+2.19j

This is matchable using shifting the resonance point to the left using additional inductance.  Check notion.
# Simple RF amp

# Impedance Matching
You're dealing with a bilateral RF amplifier, so make sure to match taking that into account. Check microwaves101.com