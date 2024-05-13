import matplotlib.pyplot as plt
import numpy as np


def draw_plot(x, y, approximations):
    for res in approximations.values():
        frame = abs(max(x) - min(x)) / 2
        x_axis = np.linspace(min(x) - frame, max(x) + frame, 500)
        phi = res[0](x_axis)
        plt.plot(x_axis, phi, label=res[1])
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.scatter(x, y, color='black', s=25)
    plt.ylim(min(y) - 1.5, max(y) + 1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(fontsize=8)
    plt.grid(True)
    plt.show()
