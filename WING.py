def closest(the_map):
    row = 0
    ts = []
    ks = None
    while row < len(the_map):
        column = 0
        while column < len(the_map[row]):
            if the_map[row][column] == "T":
                cn = (row, column)
                ts.append(cn)

            elif the_map[row][column] == "K":
                ks = (row, column)
            column += 1
        row += 1

    shortest = 100000000000000000000000000000000000000000000000000000000
    for t in ts:
        distancex = t[0] - ks[0]
        distancey = t[1] - ks[1]
        total = (distancex**2+distancey**2)**(1/2)
        if total < shortest:
            shortest = total
    return shortest

#MAIN ROUTINE
the_map = [
 ['.', '.', '.', '.', '.', '.', 'T', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', 'K', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', 'T'],
 ['.', '.', '.', '.', '.', 'T', '.', '.'],
 ['.', '.', 'T', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.']
]

print(f"{closest(the_map):.5f}")