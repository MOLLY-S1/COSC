"""Assignment Question 8"""


def get_lake_names():
    """Getting lake names until quit entered"""
    lakes = []
    lake = input("Enter lake name (or q to quit): ")
    while lake != 'q':
        lakes.append(lake)
        lake = input("Enter lake name (or q to quit): ")

    return lakes

# MAIN ROUTINE
names = get_lake_names()
print('Lakes:')
print(names)
