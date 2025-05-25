import numpy as np


def trophic_level_index(chla, tn, tp):
    """takes three parallel NumPy arrays of CHLA ,TN and TP. The function
    returns a single NumPy array in which the ith element is the TLI3 value
    computed from the ith elements of the three parameter arrays."""
    tlc = 2.22 + 2.54 * np.log10(chla)
    tln = -3.61 + 3.01 * np.log10(tn)
    tlp = 0.218 + 2.92 * np.log10(tp)
    tl13 = (tlc + tln + tlp) / 3
    return tl13
