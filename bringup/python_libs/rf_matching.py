import numpy as np
import skrf as rf
from skrf.media import DefinedGammaZ0
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def build_LNA_match_network(C1_val, L1_val, C2_val, L2_val, freq, band_ntwk, z0=50):
    # Media
    line = DefinedGammaZ0(frequency=freq, z0=z0, gamma=0j)  # zero gamma => ideal lumps

    # Lumped elements
    C1_SE  = line.capacitor(C1_val, frequency=freq, name='C1_SE')
    L1_SH = line.inductor(L1_val, frequency=freq, name='L1_SH')
    C2_SE  = line.capacitor(C2_val, frequency=freq, name='C2_SE')
    L2_SH = line.inductor(L2_val, frequency=freq, name='L2_SH')
    PORTIN = rf.Circuit.Port(frequency=freq, name='PORTIN', z0=z0)
    PORTOUT = rf.Circuit.Port(frequency=freq, name='PORTOUT', z0=z0)
    GND  = rf.Circuit.Ground(frequency=freq, name='GND', z0=z0)
    
    # Node connections
    connections = [
        [(PORTIN, 0),  (C1_SE, 0)],
        [(C1_SE, 1), (L1_SH, 0), (band_ntwk, 0)],
        [(C2_SE, 0), (L2_SH, 0), (band_ntwk, 1)],
        [(L2_SH, 1), (L1_SH, 1), (GND, 0)],
        [(PORTOUT, 0),  (C2_SE, 1)]
    ]

    ckt = rf.Circuit(connections, name='LNA-match', frequency=freq)
    return ckt



def build_T_match_network(C1_val, L_val, C2_val, freq, band_ntwk, z0=50):
    """
    Creates a 1-port Circuit:
        port1 -> series inductor -> node -> shunt capacitor -> ground
                                           -> antenna_ntwk -> ground
    using the 'media-based' approach from scikit-rf.
    
    L_val in Henries, C_val in Farads
    """
    # Media
    line = DefinedGammaZ0(frequency=freq, z0=z0, gamma=0j)  # zero gamma => ideal lumps

    # Lumped elements
    C1_SE  = line.capacitor(C1_val, frequency=freq, name='C1_SE')
    L_SH = line.inductor(L_val, frequency=freq, name='L_SH')
    C2_SE  = line.capacitor(C2_val, frequency=freq, name='C2_SE')
    PORTIN = rf.Circuit.Port(frequency=freq, name='PORTIN', z0=z0)
    GND  = rf.Circuit.Ground(frequency=freq, name='GND', z0=z0)
    # Node connections
    connections = [
        [(PORTIN, 0),  (C1_SE, 0)],
        [(C1_SE, 1), (L_SH, 0), (C2_SE, 0)],
        [(C2_SE, 1), (band_ntwk, 0)],
        [(L_SH, 1), (GND, 0)]
    ]

    ckt = rf.Circuit(connections, name='L-match', frequency=freq)
    return ckt


def build_l_match_network(L_val, C2_val, freq, band_ntwk, z0=50):
    # Media
    line = DefinedGammaZ0(frequency=freq, z0=z0, gamma=0j)  # zero gamma => ideal lumps

    # Lumped elements
    L_SH = line.inductor(L_val, frequency=freq, name='L_SH')
    C2_SE  = line.capacitor(C2_val, frequency=freq, name='C2_SE')
    PORTIN = rf.Circuit.Port(frequency=freq, name='PORTIN', z0=z0)
    GND  = rf.Circuit.Ground(frequency=freq, name='GND', z0=z0)
    # Node connections
    connections = [
        [(PORTIN, 0), (L_SH, 0), (C2_SE, 0)],
        [(C2_SE, 1), (band_ntwk, 0)],
        [(L_SH, 1), (GND, 0)]
    ]

    ckt = rf.Circuit(connections, name='L-match', frequency=freq)

    return ckt