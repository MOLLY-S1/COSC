import matplotlib.pyplot as plt
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
    chla = float_array(raw_data_dict["chla"])
    tn = float_array(raw_data_dict["tn"])
    tp = float_array(raw_data_dict["tp"])
    return trophic_level_index(chla, tn, tp)


def table_from_file(filename):
    """f"""
    # open, read and close file
    file = open(filename)
    data = file.read().splitlines()
    file.close()

    # Sort data
    proper_data = []
    headers = data[0].split(",")
    for line in data:
        line = line.split(",")
        proper_data.append(line)
    proper_data.pop(0)

    # Print and return lists
    return headers, proper_data


def load_raw_data_dict(filename):
    """sorting data into dictionary"""
    headers, data = table_from_file(filename)
    spreadsheet = {}
    i = 0
    for header in headers:

        for d in data:
            if header not in spreadsheet.keys():
                spreadsheet[header] = [d[i]]
            else:
                spreadsheet[header].append(d[i])
        i += 1
    return spreadsheet


def draw_bars_snapshot_tli3(filename):
    """Drawing bar-graphs"""
    data = load_raw_data_dict(filename)
    xs = np.arange(len(data.keys()))  # x-positions of the bars
    axes = plt.axes()
    axes.bar(xs, data[], tick_label=data.keys())
    axes.set_title("Temperatures during the week")
    axes.set_xlabel('Day of week')
    axes.set_ylabel('Temperature')
    plt.show()
