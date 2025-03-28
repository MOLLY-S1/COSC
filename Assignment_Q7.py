"""Assignment Question #7"""


def trophic_class(trophic_level_index):
    """Classing trophics"""
    if 5 <= trophic_level_index < 6:
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
    """Returning the number of lakes in a classification"""
    lakes = [1 for lake in tli3_values if
             classification == trophic_class(lake)]
    return len(lakes)


def print_trophic_class_summary(tli3_values):
    """Printing trophic class summary from lowest to highest"""
    states = ['Hypertrophic',
              'Supertrophic',
              'Eutrophic',
              'Mesotrophic',
              'Oligotrophic',
              'Microtrophic',
              'Ultra-microtrophic']
    print_list = []
    lake_num = 0
    for state in states:
        lakes = number_in_trophic_class(tli3_values, state)
        print_list.append(f"{lakes:3} lakes were {state}")
        lake_num += lakes

    print(f"Summary for the {lake_num} lakes:\n")
    for i in print_list:
        print(i)


# MAIN ROUTINE
tli3_list_1 = [4.1061, 2.54561, 4.16276,
               2.33801, 6.71792, 5.54457,
               6.49795, 2.1, 1.2, 1.4, 0.9,
               3.8, 3.0]
print_trophic_class_summary(tli3_list_1)

tli3_list_0 = [1.1, 2.1, 5.1]
print_trophic_class_summary(tli3_list_0)
