import matplotlib.pyplot as plt


def plot_voting_barchart(filename, booths):
    """f"""
    file = open(filename)
    datas = file.read().splitlines()
    datas.pop(0)
    file.close()

    # Making dict
    real = {}

    for booth in booths:
        for data in datas:
            data = list(data.split(","))
            if data[0] == booth:
                if data[1] in real:
                    real[data[1]] += int(data[2])
                else:
                    real[data[1]] = int(data[2])

    # Getting Correct Data
    heights = []
    parties = []
    for r in sorted(real):
        s = real[r]
        parties.append(r)
        heights.append(s)

    # Making Graph
    axes = plt.axes()
    axes.bar(range(len(parties)), heights, tick_label=parties)

    plt.show()


booths = ['Booth2', 'Booth3']
plot_voting_barchart("test.txt", booths)
