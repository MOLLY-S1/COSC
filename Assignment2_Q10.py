"""Program to plot TLI3 values for selected lakes"""

import matplotlib.pyplot as plt
import numpy as np


def get_input():
    """get input and check file"""
    filename = input('Input filename: ')
    while True:
        try:
            file = open(filename)
            file.close()
            return filename

        except FileNotFoundError:
            print('File does not exist.')
            filename = input('Input filename: ')


def get_lake(filename):
    """gets chosen lake"""
    data = load_raw_data_dict(filename)
    lakes = list(data.keys())
    lakes = sorted(lakes)
    lakes.remove("year")
    print('Pick a lake:')
    for lake in lakes:
        print(f"    {lake}")
    chosen_lake = input('Input lake name: ')
    while chosen_lake not in lakes:
        print('Lake name does not exist.')
        print('Pick a lake:')
        for lake in lakes:
            print(f"    {lake}")
        chosen_lake = input('Input lake name: ')
    return chosen_lake


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


def draw_time_series_fitted(filename, lake_name):
    """plots the TLI3 against time for the given lake_name and computes a
    linear fit for the data and plots this fitted data."""
    data = load_raw_data_dict(filename)
    specific_lake = float_array(data[lake_name])

    axes = plt.axes()

    xs = float_array(data["year"])
    ys = specific_lake
    axes.plot(xs, ys, marker="o", color="blue", label="actual")

    line = np.polyfit(xs, ys, 1)
    line_y = line[0] * np.array(xs) + line[1]
    axes.plot(xs, line_y, linestyle="dotted", color="green", label="fitted")

    axes.set_title(f"TLI3 over time for {lake_name}")
    axes.set_xlabel("Year")
    axes.set_ylabel('TLI3')
    axes.legend()
    plt.grid()
    plt.show()


def main():
    """Main function"""
    filename = get_input()
    lake_name = get_lake(filename)
    draw_time_series_fitted(filename, lake_name)


# MAIN ROUTINE
main()
