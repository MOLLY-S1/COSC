"""Question 28"""
import numpy as np
import matplotlib.pyplot as plt


# x=cos(vt+c−π2)

# y=cos(wt−π2)

def plot_curve(t_max, num_points, v, w, c):
    """f"""
    t = np.linspace(0, t_max, num_points)
    xs = np.cos(v*t + c - 2*np.pi)
    ys = np.cos(w*t - 2*np.pi)

    axes = plt.axes()
    axes.plot(xs, ys)
    axes.set_title(f"Curve({v}, {w}, {c})")
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    plt.show()

plot_curve(2 * np.pi, 200, 1, 3, np.pi/2)