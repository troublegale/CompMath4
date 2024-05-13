import numpy as np
import sys


def f1(x):
    return 3*x / (x**4 + 8)


def f2(x):
    return np.log(4*x + 2) / (2*x**2)


def f3(x):
    return 3*np.sin(5*x)


def test(n, x1, x2):
    if n == 1:
        f = f1
    elif n == 2:
        f = f2
    else:
        f = f3
    step = abs(x2 - x1) / 11
    a = [x1 + step*i for i in range(12)]
    with open("test", 'w') as file:
        sys.stdout = file
        for x in a:
            print(f"{x} {f(x)}")
    sys.stdout = sys.__stdout__
