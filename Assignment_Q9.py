"""Assignment Question 9"""


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


# MAIN ROUTINE
lakes = ['Lake Carrot', 'Lake Taupo', 'Lake Tekapo']
indices = get_lake_indices(lakes)
print(indices)
