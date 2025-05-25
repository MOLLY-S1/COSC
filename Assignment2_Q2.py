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

def float_array(string_list):
    """accepts a list of string values and returns a NumPy array containing
    those strings as floats."""
    floating_array = np.array(string_list, dtype=float)
    return floating_array


def raw_data_to_tli3s(raw_data_dict):
    """take a raw data dictionary and return an array of TLI3 values
    calculated using the appropriate lists of data from the dictionary."""
    chla = raw_data_dict["chla"]
    tn = raw_data_dict["tn"]
    tp = raw_data_dict["tp"]
    return trophic_level_index(chla, tn, tp)



