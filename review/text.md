Hi all,

I'm not sure if this is the correct subreddit to post this, I'm trying to design a cascode LNA and quickly put-together single-transistor amplifier to experiment with.

I posted pictures of the designs and the ltspice plots (S-parameters and input, output impedances), the amplifier is meant to work at 868 MHz.

I mainly want to make sure there is actually a chance the amplifier works based on the simulations before I send the design over to the manufacturer:
- Impedance matching: Are the input and output impedance too far off from 50 ohms to be able to match effectively? I expect the match in simulation to be off from the real match.
- Amplifier component size. The RF-path is about 25 mm, which is already a large chunk of the 868 MHz wavelength. (185 mm in FR4) So should I account for the phase-shift / transmission-line loss when matching? If so what is the best way to account for it?
- Rollet stability factor is greater than 1 across the entire region for the cascode, for the single-transistor amplifier there's a resonance happening right around 868 MHz, and rollet goes below 1. What's the best way to fix this?

And finally:
- Is there anything else I might have overlooked which I'd really need to fix before I send this to production?

Thanks a million!