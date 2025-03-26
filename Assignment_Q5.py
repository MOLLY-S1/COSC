"""Question #3"""

def number_in_trophic_class(tli3_values, classification) :
    """Returns the number of lakes in trophic class"""
    lakes = 0
    for trophic_level_index in tli3_values:
        if 5 <= trophic_level_index < 6:
            classified = "Supertrophic"
        elif 4 <= trophic_level_index < 5:
            classified = "Eutrophic"
        elif 3 <= trophic_level_index < 4:
            classified = "Mesotrophic"
        elif 2 <= trophic_level_index < 3:
            classified = "Oligotrophic"
        elif 1 <= trophic_level_index < 2:
            classified = "Microtrophic"
        elif trophic_level_index < 1:
            classified = "Ultra-microtrophic"

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
