"""Assignment Question 11 - Challenge Question"""


def trophic_class(trophic_level_index):
    """Classing trophic levels"""
    if 6 <= trophic_level_index:
        classification = "Hypertrophic"
        return classification
    elif 5 <= trophic_level_index < 6:
        classification = "Supertrophic"
        return classification
    elif 4 <= trophic_level_index < 5:
        classification = "Eutrophic"
        return classification
    elif 3 <= trophic_level_index < 4:
        classification = "Mesotrophic"
        return classification
    elif 2 <= trophic_level_index < 3:
        classification = "Oligotrophic"
        return classification
    elif 1 <= trophic_level_index < 2:
        classification = "Microtrophic"
        return classification
    elif trophic_level_index < 1:
        classification = "Ultra-microtrophic"
        return classification


def number_in_trophic_class(tli3_values, classification):
    """Returns the number of lakes in trophic class"""
    lakes = 0

    for lake in tli3_values:
        classified = trophic_class(lake)
        if classified == classification:
            lakes += 1

    return lakes


def print_summary(print_list, total_area):
    """Printing lake values summary"""
    # Printing Items
    print("Area summary\n"
          "-----------------------------")
    for item in print_list:
        print(item)
    print(f"-----------------------------\n"
          f"Total lake area       {total_area} sq m")


def print_lake_report(lake_state_map):
    """Takes a list of strings representing the water quality across a lake
    and prints a summary showing the amount of the lake that is at each
    trophic class"""
    full_water_list = list(lake_state_map)
    # Split into each value
    split_water_list = []
    for area in full_water_list:
        values = list(area)
        split_water_list.append(values)

    # Split into final water list
    final_water = []
    for split_water in split_water_list:
        water_area = list(split_water)
        for area in water_area:
            if area != " ":
                final_water.append(int(area))

    # Printing Summary
    states = ['Hypertrophic',
              'Supertrophic',
              'Eutrophic',
              'Mesotrophic',
              'Oligotrophic',
              'Microtrophic',
              'Ultra-microtrophic']

    printing_list = []
    lake_area = 0
    for state in states:
        lakes = number_in_trophic_class(final_water, state)
        printing_list.append(f"{state:<20}{lakes:>4} sq m")
        lake_area += lakes

    return print_summary(printing_list, lake_area)


# MAIN ROUTINE
lake_map = [
    '   4210000  ',
    '  543210000 ',
    '  433210000 ',
    '   2110000  ',
]
print_lake_report(lake_map)
print()
lake_map = [
    '     99888        ',
    '    87654345      ',
    '  76543212345     ',
    ' 6543210123456    ',
    ' 4321000012345    ',
    '  432100001234    ',
    '    3210000123    ',
    '       210000     '
]
print_lake_report(lake_map)
