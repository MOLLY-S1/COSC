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
    """Making lists from file data"""
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


def draw_bars_tli3_by_region(filename, region):
    """Drawing the bar graph of lakes within region"""
    # Loading data and tli3 values
    data = load_raw_data_dict(filename)
    tli3_values = raw_data_to_tli3s(data)

    # Finding lakes in region
    regions = data["lake_region"]
    lake_names = []
    regional_tli3 = []
    for i in range(len(regions)):
        if regions[i] == region:
            lake_names.append(data["lake_name"][i])
            regional_tli3.append(tli3_values[i])

    xs = np.arange(len(regional_tli3))  # x-positions of the bars

    # Plotting
    axes = plt.axes()
    axes.bar(xs, regional_tli3, tick_label=lake_names, color="indigo")
    axes.tick_params(axis='x', labelrotation=90)
    axes.set_title(f"Snapshot TLI3s from {filename} - {region}")
    axes.set_xlabel('Lake')
    axes.set_ylabel('TLI3')
    plt.tight_layout()
    plt.show()
