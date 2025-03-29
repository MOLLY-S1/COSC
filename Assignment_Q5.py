"""Question #3"""


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


# MAIN ROUTINE
tli3_list_1 = [4.1061, 2.54561, 4.16276,
               2.33801, 6.71792, 5.54457,
               6.49795, 2.1, 1.2, 1.4, 0.9,
               3.8, 3.0]
number = number_in_trophic_class(tli3_list_1, 'Microtrophic')
print(f'{number} were Microtrophic.')

tli3_list_1 = [4.1061, 2.54561, 4.16276,
               2.33801, 6.71792, 5.54457,
               6.49795, 2.1, 1.2, 1.4, 0.9,
               3.8, 3.0, 3.77]
number = number_in_trophic_class(tli3_list_1, 'Mesotrophic')
print(f"{number} were Mesotrophic.")
