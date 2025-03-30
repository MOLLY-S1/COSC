"""Assignment Question 10"""


def get_lake_names():
    """Getting lake names until quit entered"""
    lakes = []
    lake = input("Enter lake name (or q to quit): ")
    while lake != 'q':
        lakes.append(lake)
        lake = input("Enter lake name (or q to quit): ")

    return lakes


def get_lake_indices(lake_names):
    """Takes input for tli value for all lakes in list"""
    i = 0
    tli_list = []
    while i < len(lake_names):
        for lake in lake_names:
            tli = float(input(f"Enter TLI for {lake}: "))
            tli_list.append(tli)
            i += 1

    return tli_list


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
    else:
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

    print(f"Summary for the {lake_num} lakes:")
    for i in print_list:
        print(i)


def main():
    """Main function to include all other calls. Asks the user to enter a
    series of lake names then asks the user to enter a TLI value for each lake.
    The function then prints out the water quality level for each lake,
    followed by a summary showing the number lakes at each trophic class"""
    # Get lake names
    lakes = get_lake_names()
    print()

    # Get lake indices
    indices = get_lake_indices(lakes)
    print()

    # Print Lake water summary
    print("Water quality summary\n"
          "---------------------")
    i = 0
    while i < len(lakes):
        for tli in indices:
            classification = trophic_class(tli)
            print(f"{lakes[i]}: {classification}")
            i += 1
    print()

    # Print the classification for the lakes
    print_trophic_class_summary(indices)
    print()


# MAIN ROUTINE
main()
