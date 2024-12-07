# Vias
Make sure the ground plane is very well connected.

# Power supply
## Decoupling capacitors
- Add some decoupling capacitors for the power supply
- In example 10 uF + 100 nF + 100 pF was added + a ferrite bead

# Measuring
## Impedance 
An impedance is simply a voltage divided by a current.
- Connect a single SMA cable to the relevant connector, check the smith chart and tune the matching network until the impedance is exactly 50 ohms.

- In case of an existing delay in the cable, make sure to account for that by setting a delay.

## Protection
- Check how to protect your device from too much powers
    - perhaps adding an attenuator?

# Coplanar waveguide vs microstrip
Think about whether you'd use 
- a coplanar waveguide (so a copper strip separated by 2 ground planes on each side)
- a microstrip line: a single copper stripline with a ground plane below.


# TODO:
- https://www.youtube.com/watch?v=9ZoO_AABzqU

- Check the feedback mechanism
    - How can I trade-off gain for bandwidth in order to use this LNA for frequencies up to 10 GHz?
    - Assuming you want to keep this LNA to a size of 30 x 40
- Check the antenna you want to put next to the board
    - Meandering of an F-antenna
    - Ground plane required for this antenna