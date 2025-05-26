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


def load_raw_data_dict(filename):
    """take the name of a csv file, containing columns of data, and return a
    dictionary representation of said data."""
    full_data = {}
    file = open(filename)
    data = file.read().splitlines()
    print(data)

    file.close()
    headers = data[0]
    headers = list(headers.split(","))
    for header in headers:
        full_data[header] = []
    print(headers)
    print(len(headers), "headers len")


    for i in range(1,len(headers)-1):
        specific = list(data[i].split(","))
        print("specific", specific)
        print(i)
        for i in range(len(specific)):
            if headers[i] in full_data.keys():
                full_data[headers[i]].append(list(specific[i][i]))
            else:
                full_data[headers[i]] = [(list(specific[i]))]


    return full_data


result = load_raw_data_dict('r.txt')
for col_name, data in result.items():
    print(f"'{col_name}': {data}")