import math
import sys
import numpy as np


def f(x):
    return 3*x / (x**4 + 8)


def phi(x):
    return 0.136*x - 0.104


def phi_square(x):
    return 2.521*x**2 + 6.383*x + 3.094


a = [-2 + 0.2 * i for i in range(11)]

s = sum((phi_square(x) - f(x))**2 for x in a)
sko = math.sqrt(s / len(a))
print(sko)
