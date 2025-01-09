# Components
- Are the capacitors and inductors good enough for these frequencies? (Murata)
    - There's not much mentioned in the datasheet.
    - C1550 these ones were used by phil's lab.
    - C27123 were the inductors used by phil's lab (sunlord). (https://media.digikey.com/pdf/Data%20Sheets/Shenzhen%20Sunlord/SDCL-D.pdf)
    
# On impedance matching
The input and output impedances for both amplifiers are quite far off from 50 ohms, which will make impedance matching quite challenging.
Ideally the impedance should be brought down to something in between 20 and 200 ohms.
We do decide to give it a go however.