import matplotlib.pyplot as plt
import numpy as np


def draw_plot(x, approximations):
    for res in approximations.values():
        x_axis = np.linspace(min(x) - 2, max(x) + 2, 500)
        phi = res[0](x_axis)
        plt.plot(x_axis, phi, label=res[1])
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()