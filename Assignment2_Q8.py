import matplotlib.pyplot as plt
import numpy as np


def float_array(string_list):
    """accepts a list of string values and returns a NumPy array containing
    those strings as floats."""
    floating_array = np.array(string_list, dtype=float)
    return floating_array


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


def draw_time_series_single(filename, lake_name):
    """accepts the name of a file alongside a lake name and plots a line
    graph of TL3 over time for the specified lake."""
    data = load_raw_data_dict(filename)
    specific_lake = float_array(data[lake_name])

    xs = float_array(data["year"])
    ys = specific_lake

    # Plotting
    axes = plt.axes()
    axes.plot(xs, ys)
    axes.set_title(f"TLI3 over time for {lake_name}")
    axes.set_xlabel("Year")
    axes.set_ylabel('TLI3')
    plt.grid()
    plt.show()



