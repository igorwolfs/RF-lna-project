# Electrical characteristics
## Max input signal voltage

Assume a max input voltage of 1 mV (close to the transceiver) at 868 MHz.
Given a gain of 25 dB

## Current variation

Current amplitude is somewhere between 18.4 -> 25.6 mA at the oscillation frequency (which is pretty huge).

So required charge over half a period is (25.6-18.4) * (T/2) =  (25.6-18.4)e-3/ (868e6 * 2) = 4.15 pC

Make sure the capacitor arrays carry at least that amount of charge at 5 V.

## Max voltage

- Supply voltage: 5 V

## Max power

# Components
## Matching
**Left Circuit**
- L-circuit
**Right circuit**
- T-circuit (2 caps), to match + to keep from shorting to ground
- 2 capacitors
- 2 inductors (see SimNec)
## Transistors
- BFP640 x 3
- 7 resistors
    - 2.2 kOhm
    - 1 kOhm x 2
    - 200 Ohms x 2
    - 0 Ohms
    - 50 Ohms

## Capacitors
- Filter: 100 nF
- Decoupling: Simply look for low-frequency capacitance, check the curves
    - 100 pF
    - 100 nF
    - 1 uF

# JLCPCB Part availability
### Capacitor availability
Availability
Capacitor:
- 10 pF
- 12 pF
- 15 pF
- 18 pF
- 47 pF
### Inductor availability
Inductor:
- 68 nH
- 3.9 nH
- 5.1 nH
- 6.2 nH
- 15 nH
- 10 nH
- 470 nH

### 5 V power regulator