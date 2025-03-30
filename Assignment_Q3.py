def print_variables_over_time(c_0, tn_0, tp_0, percent_reduction, final_year):
    """Printing forcast table of values"""

    print("Year    CHLA       TN        TP")
    year = 0
    print(f"{year:3}{c_0:10.2f}{tn_0:10.2f}{tp_0:10.2f}")
    while year < final_year:
        year += 1
        c_0 = c_0*((100-percent_reduction)/100)
        tn_0 = tn_0*((100-percent_reduction)/100)
        tp_0 = tp_0*((100-percent_reduction)/100)
        print(f"{year:3}{c_0:10.2f}{tn_0:10.2f}{tp_0:10.2f}")



# MAIN ROUTINE
print_variables_over_time(128, 1024, 256, 6.25, 10)

