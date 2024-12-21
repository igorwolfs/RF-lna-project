# Electrical characteristics
## Max input signal voltage

Assume a max input voltage of 1 mV (close to the transceiver) at 868 MHz.
Given a gain of 25 dB

## Current variation

Current amplitude is somewhere between 18.4 -> 25.6 mA at the oscillation frequency (which is pretty huge).

So required charge over half a period is (25.6-18.4) * (T/2) =  (25.6-18.4)e-3/ (868e6 * 2) = 4.15 pC

Make sure the capacitor arrays carry at least that amount of charge at 5 V.
So 4.15 pC / 5 V < 1 pF, so the capacitor needs to be at least 1 pF (easy).


## Max voltage

- Supply voltage: 5 V


# Components

## Power supply
- L78L05, basic component (jlcpcb)

## LED
- Add a cheap LED somewhere to see whether the supply voltage is in fact 5 V
NOTE: take a basic part here for cheaper assembly.

## Resistors
- Always choose smallest package with relevant power rating, to minimize parasitics.
- Probably good up to a few GHz, once going above 2 GHz make sure to get specialized once.

## Capacitors
Capacitor Q-factor: capacitor's reactance / capacitor's parasitic resistance.
- The bigger Q, the smaller the ESR relative to the reactance, the better.

## AC blocking inductors
Finding a good AC blocking inductor that is
- About 100 nH
- Self resonant-frequency beyond 2 GHz
Seems to be quite the task

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
Use Murata or Vishay for impedance matching components.


### Capacitor availability

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