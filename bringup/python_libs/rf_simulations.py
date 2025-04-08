import os
import re
import skrf as rf
import numpy as np


def load_s2p_files(data_dir):
	# Ensure the directory exists
	if not os.path.exists(data_dir):
		raise FileNotFoundError(f"Directory {data_dir} does not exist.")

	# List all files in the directory
	print(f"Loading files from: {data_dir}")
	print(f"list directory: {os.listdir(data_dir)}")

	pattern = re.compile(
		r'^BFP640(_w_noise)?_VCE_([\d\.]+)V_IC_([\d\.]+)mA\.s2p$',
		re.IGNORECASE
	)

	# Dictionary to store the data
	# We'll use a tuple key: (VCE_float, IC_float, noise_bool)
	# Each value is the corresponding rf.Network
	networks = {}

	# Iterate over all files in the directory
	for fname in os.listdir(data_dir):
		# Only consider .s2p files
		if not fname.lower().endswith('.s2p'):
			continue

		match = pattern.match(fname)
		if match:
			noise_str, vce_str, ic_str = match.groups()
			# Convert text to numeric
			vce_val = float(vce_str)
			ic_val = float(ic_str)
			noise_bool = (noise_str is not None)  # True if "_w_noise" was present

			# Load the network
			full_path = os.path.join(data_dir, fname)
			ntwk = rf.Network(full_path)

			# Store it in the dictionary
			# Key: (VCE, IC, noise_flag)
			networks[(vce_val, ic_val, noise_bool)] = ntwk
	return networks

def find_bounding_networks(networks, vce_target, ic_target):

    # 1) Collect all VCE, IC from the dictionary that match the noise flag
	valid_biases = []
	for (vce_val, ic_val, noise), ntwk in networks.items():
		valid_biases.append((vce_val, ic_val, noise))
		# if (noise_flag == noise):
		# valid_biases.append((vce_val, ic_val))

    # 2) Separate out unique sorted VCE, IC
    #    We'll find the "just below or equal" and "just above or equal" values for each axis
	unique_vce = sorted(set([b[0] for b in valid_biases]))
	unique_ic  = sorted(set([b[1] for b in valid_biases]))

    # Helper to find the largest value <= target, and the smallest value >= target
	def find_bounds(values, target):
		below = [v for v in values if v <= target]
		above = [v for v in values if v >= target]
		v_below = max(below) if below else None
		v_above = min(above) if above else None
		return v_below, v_above

	vce_below, vce_above = find_bounds(unique_vce, vce_target)
	ic_below,  ic_above  = find_bounds(unique_ic,  ic_target)

    # 3) Construct up to 4 corners from {vce_below, vce_above} × {ic_below, ic_above}
    #    Some might be None if we don't have a bounding value on that side.
	corners = []
	for vce_candidate in (vce_below, vce_above):
		for ic_candidate in (ic_below, ic_above):
			if vce_candidate is not None and ic_candidate is not None:
				if (networks.get((vce_candidate, ic_candidate, 0)) is not None):
					corners.append((vce_candidate, ic_candidate, 0)) # Add both with and without noise flag
				if (networks.get((vce_candidate, ic_candidate, 1)) is not None):
					corners.append((vce_candidate, ic_candidate, 1))
	print(f"corners: {corners}")
	# 4) Look up each corner in the dictionary if it exists
	bounding = {}
	for (vc, ic, noise) in corners:
		if (vc, ic, noise) in networks:
			bounding[(vc, ic, noise)] = networks[(vc, ic, noise)]
		else:
			print(f"Not in networks?")
	return bounding


def interpolate_2d_network(network_dict, target_vce, target_ic, interp_kind='linear'):
    """
    Interpolate a Network from a dictionary of 2-Port Networks with different Vce and Ic values.
    
    Parameters
    ----------
    network_dict : dict
        Dictionary with keys as tuples (Vce, Ic, noise_flag) and values as skrf.Network objects
    target_vce : float
        Target Vce value to interpolate for
    target_ic : float
        Target Ic value to interpolate for
    interp_kind : str, optional
        Interpolation method ('linear', 'cubic', etc.), default is 'linear'
        
    Returns
    -------
    ntw : skrf.Network
        Interpolated network at the specified Vce and Ic
        
    Notes
    -----
    This function handles 1D or 2D interpolation depending on the available data points.
    If only one Vce or Ic value is available, it will perform 1D interpolation along the other axis.
    This function ignores any noise flag in the dictionary keys and uses all available measurements.
    """
    import numpy as np
    from scipy.interpolate import interp1d, RegularGridInterpolator
    
    # Create a simplified dictionary that ignores the noise flag
    simplified_dict = {}
    for key, network in network_dict.items():
        # Extract just Vce and Ic from the key
        simplified_key = (key[0], key[1])
        # If we have multiple networks for the same Vce/Ic (due to different noise flags),
        # just use the last one encountered
        simplified_dict[simplified_key] = network
    
    # Extract unique Vce and Ic values
    vce_values = sorted(set([key[0] for key in simplified_dict.keys()]))
    ic_values = sorted(set([key[1] for key in simplified_dict.keys()]))
    
    # Get a reference network to copy frequency information, etc.
    reference_key = list(simplified_dict.keys())[0]
    reference_network = simplified_dict[reference_key]
    result_network = reference_network.copy()
    
    # Get the shape of s-parameters
    s_shape = reference_network.s.shape
    
    # Handle different interpolation cases
    if len(vce_values) == 1 and len(ic_values) == 1:
        # Only one unique Vce/Ic combination, no interpolation needed
        return reference_network.copy()
    
    elif len(vce_values) == 1:
        # 1D interpolation along Ic axis
        vce = vce_values[0]
        s_params = []
        
        for ic in ic_values:
            key = (vce, ic)
            if key in simplified_dict:
                s_params.append((ic, simplified_dict[key].s))
        
        s_params.sort(key=lambda x: x[0])  # Sort by Ic
        ic_points = [x[0] for x in s_params]
        s_data = np.array([x[1] for x in s_params])
        
        # Perform 1D interpolation for each s-parameter component
        f = interp1d(ic_points, s_data, axis=0, kind=interp_kind, bounds_error=False, fill_value="extrapolate")
        result_network.s = f(target_ic)
        
    elif len(ic_values) == 1:
        # 1D interpolation along Vce axis
        ic = ic_values[0]
        s_params = []
        
        for vce in vce_values:
            key = (vce, ic)
            if key in simplified_dict:
                s_params.append((vce, simplified_dict[key].s))
        
        s_params.sort(key=lambda x: x[0])  # Sort by Vce
        vce_points = [x[0] for x in s_params]
        s_data = np.array([x[1] for x in s_params])
        
        # Perform 1D interpolation for each s-parameter component
        f = interp1d(vce_points, s_data, axis=0, kind=interp_kind, bounds_error=False, fill_value="extrapolate")
        result_network.s = f(target_vce)
        
    else:
        # 2D interpolation over Vce and Ic
        # First, we need to ensure we have complete data for all Vce/Ic combinations
        # Create a grid of all possible Vce/Ic combinations
        vce_ic_grid = {}
        for vce in vce_values:
            for ic in ic_values:
                vce_ic_grid[(vce, ic)] = None
        
        # Fill in the grid with available networks
        for key, network in simplified_dict.items():
            vce_ic_grid[key] = network
        
        # Check if we have missing data points
        missing_points = [key for key, val in vce_ic_grid.items() if val is None]
        if missing_points:
            # Fill missing points with nearest available data
            # This is a simple approach; more sophisticated methods could be used
            for missing_key in missing_points:
                # Find the closest available network
                min_distance = float('inf')
                closest_key = None
                missing_vce, missing_ic = missing_key
                
                for key, network in simplified_dict.items():
                    vce, ic = key
                    # Calculate Euclidean distance in the Vce/Ic space
                    distance = ((vce - missing_vce)**2 + (ic - missing_ic)**2)**0.5
                    if distance < min_distance:
                        min_distance = distance
                        closest_key = key
                
                # Use the closest network for the missing point
                vce_ic_grid[missing_key] = simplified_dict[closest_key]
        
        # Create arrays for the s-parameters
        s_data = np.zeros((len(vce_values), len(ic_values), *s_shape[:]), dtype=complex)
        vce_indices = {vce: i for i, vce in enumerate(vce_values)}
        ic_indices = {ic: i for i, ic in enumerate(ic_values)}
        
        # Populate the s_data array
        for (vce, ic), network in vce_ic_grid.items():
            if network is not None:  # This check shouldn't be necessary now, but just in case
                i, j = vce_indices[vce], ic_indices[ic]
                s_data[i, j] = network.s
        
        # Perform 2D interpolation for each frequency point and s-parameter component
        result_s = np.zeros(s_shape, dtype=complex)
        
        # For each frequency point
        for f_idx in range(s_shape[0]):
            # For each port pair
            for i in range(s_shape[1]):
                for j in range(s_shape[2]):
                    # Real part interpolation
                    real_data = s_data[:, :, f_idx, i, j].real
                    real_interp = RegularGridInterpolator(
                        (vce_values, ic_values), 
                        real_data,
                        method=interp_kind,
                        bounds_error=False,
                        fill_value=None
                    )
                    
                    # Imaginary part interpolation
                    imag_data = s_data[:, :, f_idx, i, j].imag
                    imag_interp = RegularGridInterpolator(
                        (vce_values, ic_values),
                        imag_data,
                        method=interp_kind,
                        bounds_error=False,
                        fill_value=None
                    )
                    
                    # Combine real and imaginary parts
                    pts = np.array([[target_vce, target_ic]])
                    result_s[f_idx, i, j] = real_interp(pts)[0] + 1j * imag_interp(pts)[0]
        
        result_network.s = result_s
    
    # Update the network name to reflect the interpolated values
    result_network.name = f"Interp_VCE_{target_vce:.2f}V_IC_{target_ic:.2f}mA"
    
    return result_network


def convert_port_2to3_ce(transistor_2port, I_E, V_T=0.026): # ASSUME V_T = 26e-3
    """
    Converts a 2-port transistor S-parameter network into a 3-port system
    where the emitter is explicitly represented as the third port connected to ground.
    
    Parameters:
        transistor_2port (rf.Network): The original 2-port transistor S-parameter network.
    
    Returns:
        rf.Network: A new 3-port Network with the emitter explicitly represented.
    """
    # Extract frequency information from the original network
    freq = transistor_2port.frequency
    Z0 = transistor_2port.z0

    # Initialize a new 3-port S-matrix with emitter grounded
    s_3port = np.zeros((freq.npoints, 3, 3), dtype=complex)

    # Populate the original S-parameters into the new matrix
    s_3port[:, :2, :2] = transistor_2port.s


    # Approximate intrinsic emitter resistance
    r_e = (V_T / I_E) * np.ones_like(s_3port[:, 0, 0]) # V_T = 26mV
    print( np.ones_like(s_3port[:, 0, 0]))
    print(Z0[0])
    z0_arr = np.ones_like(s_3port[:, 0, 0]) * Z0[0][0] # Assume ssame Z0 for all ports
    S_em_11 = r_e / (2*z0_arr + r_e)
    S_em_21 = 2*z0_arr[0] / (2*z0_arr+ r_e)
    s_3port[:, 2, 2] = S_em_11       # self reflection at emitter port.
    
    # The coupling from emitter to the other ports is given by S21_em.
    s_3port[:, 0, 2] = S_em_21        # coupling from port 0 (base) to emitter.
    s_3port[:, 1, 2] = S_em_21        # coupling from port 1 (collector) to emitter.

    # And by reciprocity, the coupling from emitter back to ports 0 and 1:
    s_3port[:, 2, 0] = S_em_21
    s_3port[:, 2, 1] = S_em_21


    z0_new = np.array([Z0[:,0], Z0[:,1], Z0[:,0]]).reshape(Z0.shape[0], 3)


    # Create a new Network for the 3-port system
    transistor_3port = rf.Network(
        frequency=freq,
        s=s_3port,
        name = transistor_2port.name,
        z0=z0_new  # Assume same Z0 for all ports
    )

    return transistor_3port


DBG = False


def convert_ce2cb(ce_ntwk):
    # Input must be a 3-port CE network
    if ce_ntwk.s.shape[1] != 3 or ce_ntwk.s.shape[2] != 3:
        raise ValueError("The input network must be a 3-port network.")
    S_reordered = np.zeros_like(ce_ntwk.s)
    ce_denom = 1 / (1 + ce_ntwk.s[:, 0, 0])
    S_reordered[:, 0, 0] = ce_ntwk.s[:, 2, 2] - (ce_ntwk.s[:, 2, 1] * ce_ntwk.s[:, 1, 2]) * ce_denom
    S_reordered[:, 0, 1] = ce_ntwk.s[:, 2, 1] - (ce_ntwk.s[:, 2, 0] * ce_ntwk.s[:, 0, 1]) * ce_denom
    S_reordered[:, 1, 0] = ce_ntwk.s[:, 1, 2] - (ce_ntwk.s[:, 1, 0] * ce_ntwk.s[:, 0, 2]) * ce_denom
    S_reordered[:, 1, 1] = ce_ntwk.s[:, 1, 1] - (ce_ntwk.s[:, 1, 0] * ce_ntwk.s[:, 0, 1]) * ce_denom
    S_reordered[:, 2, 2] = -1 # SHORT

    Z0 = ce_ntwk.z0 # ASSUME ALL Z0 the same
    z0_new = np.array([Z0[:,0], Z0[:,1], Z0[:,0]]).reshape(Z0.shape[0], 3)


    ntwk_cb = ce_ntwk.copy()
    ntwk_cb.s = S_reordered
    ntwk_cb.name = ce_ntwk.name + "_cb_convert"
    ntwk_cb.z0 = z0_new
    return ntwk_cb


def convert_ce2cc(ce_ntwk):
    # Input must be a 3-port CE network
    if ce_ntwk.s.shape[1] != 3 or ce_ntwk.s.shape[2] != 3:
        raise ValueError("The input network must be a 3-port network.")
    S_reordered = np.zeros_like(ce_ntwk.s)
    cc_denom = 1 / (1 + ce_ntwk.s[:, 1, 1])
    S_reordered[:, 0, 0] = ce_ntwk.s[:, 0, 0] - (ce_ntwk.s[:, 0, 1] * ce_ntwk.s[:, 1, 0]) * cc_denom
    S_reordered[:, 0, 1] = ce_ntwk.s[:, 0, 2] - (ce_ntwk.s[:, 0, 1] * ce_ntwk.s[:, 1, 2]) * cc_denom
    S_reordered[:, 1, 0] = ce_ntwk.s[:, 2, 0] - (ce_ntwk.s[:, 2, 1] * ce_ntwk.s[:, 1, 0]) * cc_denom
    S_reordered[:, 1, 1] = ce_ntwk.s[:, 2, 2] - (ce_ntwk.s[:, 2, 1] * ce_ntwk.s[:, 1, 2]) * cc_denom
    S_reordered[:, 2, 2] = -1 # SHORT

    Z0 = ce_ntwk.z0 # ASSUME ALL Z0 the same
    z0_new = np.array([Z0[:,0], Z0[:,1], Z0[:,0]]).reshape(Z0.shape[0], 3)


    ntwk_cc = ce_ntwk.copy()
    ntwk_cc.s = S_reordered
    ntwk_cc.name = ce_ntwk.name + "_cc_convert"
    ntwk_cc.z0 = z0_new
    return ntwk_cc