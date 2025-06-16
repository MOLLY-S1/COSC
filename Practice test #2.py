def item_locations(filename):
    """f"""
    # Get data
    file = open(filename)
    data = file.read().splitlines()
    file.close()

    # Make into a single list
    r_data = []
    for d in data:
        line = d.split(",")
        r_line = []
        for l in line:
            l = l.split(": ")
            for m in l:
                r_line.append(m)
        r_data.append(r_line)

    # Make into dict
    findings = {}
    for r in r_data:
        x, y, name = r
        tup = (x, y)
        if name in findings.keys():
            findings[name].append(tup)
        else:
            findings[name] = [tup]

    return findings



location_dict = item_locations('test.txt')
for item, locations in location_dict.items():
    print(f"{item}: {locations}")

