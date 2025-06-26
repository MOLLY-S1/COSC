import matplotlib.pyplot as plt
import numpy as np


def histogram_of_speeds(filename):
    """f"""
    # get data
    file = open(filename)
    data = file.read().splitlines()
    file.close()
    del data[0:2]
    header = list(data[0].split(","))
    name = header[0]
    del data[0:7]

    speed = []
    for line in data:
        l = line.split(",")
        speed.append(float(l[4]))

    ys = np.array(speed)

    axes = plt.axes()
    axes.hist(ys, bins=range(0, 31, 1), density=True)
    axes.grid(True)
    axes.set_title(f'Wind speed distribution {name}')
    axes.set_xlabel('Speed (m/s)')
    axes.set_ylabel('Proportion')
    plt.show()


histogram_of_speeds("winddata.txt")
