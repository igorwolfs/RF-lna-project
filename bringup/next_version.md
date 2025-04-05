# Next version
- Make sure to add RF test-pads at the point of testing
	- Add a u.fl. test-pad in production.
	- Using a switchable coax connector (like the [MM8030-2610RK0
](https://eu.mouser.com/ProductDetail/Murata-Electronics/MM8030-2610RK0?qs=%2Fha2pyFadui6EZC%252BNwU5I446m3Z%2FkahugdGMg7kp0Gd%252Bvd0%252BzP64YA%3D%3D)) which is placed in series with the transmission line and enabled when a coax is connected to it.
- Make sure to add 2 testpoints if necessary
	- One near transceiver
	- One near the antenna (to check your transmission line)
- Never manually try soldering 0402-components again, always use 0603 for matching. Make sure there is a default 0402 blocking capacitor in place.
- Make sure to take into account possible drops in supply voltage due to LDO inaccuracy. (or choose more accurate LDO's for simulation)
- Make sure your antenna simulation is accurate enough (e.g.: include stitched ground planes in sim)
- Make sure your HF-SS transistor simulation is accurate (use Qucs, Sckit-RF)

## Future projects
- [Oscillator measuring](https://youtu.be/G9zZRNzhsEE?si=bZdA5BlI5b6n5sOV)

# Sources:
- [Stackoverflow, placing RF testpoints](https://electronics.stackexchange.com/questions/560225/where-should-i-place-my-rf-test-point?fbclid=IwY2xjawJbKZVleHRuA2FlbQIxMAABHawI_kbqkomStI-Y4tLwu_u_v19jUvDQYggQsGq0M43ViGhQL__Cy7Yblg_aem_1vwwciJbDrnEQNaRCisDlQ)