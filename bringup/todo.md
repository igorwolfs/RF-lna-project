# TODO
## Antenna Check
- Make sure to check antenna S-parameters with
	- Single port calibration
	- Calibration with connector measurement, not coax
	- Direct connector.

It seems like the difference when using a coax cable for calibration and measurement, even after calibration is about 100 MHz off from the expected value.

## Buy
- An additional coax but shorter (5 cm instead of 33 cm)
- An additional load end for calibration
- Buy a DC blocking circuit for use with the LiteVNA

## LNA
- Take all python functions out-of the jupyter notebooks and put them into a common library for importing
