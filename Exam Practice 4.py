"""Question 29"""
import numpy as np
import matplotlib.pyplot as plt


def get_in():
    """f"""
    filename = input("Enter filename: ")
    file = open(filename)
    data = file.read().splitlines()
    data.pop(0)
    file.close()
    return data, filename


def sorting(data):
    """f"""
    cycles = []
    for line in data:
        line = line.split(";")
        cycles.append(int(line[1]))

    return cycles


def graphing(cycles, filename):
    """f"""
    print(len(cycles))
    ys = np.array(cycles)
    print(ys)
    xs = np.arange(1, len(cycles) + 1)

    title = filename.replace(".csv", "").replace(".txt", "")

    line = np.polyfit(xs, ys, 1)
    line_y = line[0] * np.array(xs) + line[1]

    axes = plt.axes()
    axes.plot(xs, ys, label="Cycleway usage")
    axes.plot(xs, line_y, linestyle=":", label="Fitted lines")
    axes.set_title(f"{title}")
    axes.legend()
    axes.set_xlabel("Week number")
    axes.set_ylabel("Cycle count")
    axes.grid(True)
    plt.show()


def main():
    data, filename = get_in()
    cycles = sorting(data)
    graphing(cycles, filename)


main()
