from numpy import exp, log

from systems import solve_system


def linear_approximation(xs, ys):
    n = len(xs)
    sx = sum(xs)
    sxx = sum(x ** 2 for x in xs)
    sy = sum(ys)
    sxy = sum(x * y for x, y in zip(xs, ys))

    a, b = solve_system(
        [
            [n, sx],
            [sx, sxx]
        ],
        [sy, sxy])
    return lambda xi: a + b*xi, (a, b)


def quadratic_approximation(xs, ys):
    n = len(xs)
    sx = sum(xs)
    sxx = sum(x ** 2 for x in xs)
    sxxx = sum(x ** 3 for x in xs)
    sxxxx = sum(x ** 4 for x in xs)
    sy = sum(ys)
    sxy = sum(x * y for x, y in zip(xs, ys))
    sxxy = sum(x * x * y for x, y in zip(xs, ys))
    a, b, c = solve_system(
        [
            [n, sx, sxx],
            [sx, sxx, sxxx],
            [sxx, sxxx, sxxxx]
        ],
        [sy, sxy, sxxy]
    )
    return lambda xi: a + b*xi + c*xi**2, (a, b, c)


def cubic_approximation(xs, ys):
    n = len(xs)
    sx = sum(xs)
    sxx = sum(x ** 2 for x in xs)
    sxxx = sum(x ** 3 for x in xs)
    sxxxx = sum(x ** 4 for x in xs)
    sxxxxx = sum(x ** 5 for x in xs)
    sxxxxxx = sum(x ** 6 for x in xs)
    sy = sum(ys)
    sxy = sum(x * y for x, y in zip(xs, ys))
    sxxy = sum(x * x * y for x, y in zip(xs, ys))
    sxxxy = sum(x * x * x * y for x, y in zip(xs, ys))
    a, b, c, d = solve_system(
        [
            [n, sx, sxx, sxxx],
            [sx, sxx, sxxx, sxxxx],
            [sxx, sxxx, sxxxx, sxxxxx],
            [sxxx, sxxxx, sxxxxx, sxxxxxx]
        ],
        [sy, sxy, sxxy, sxxxy]
    )
    return lambda xi: a + b*xi + c*xi**2 + d*xi**3, (a, b, c, d)


def exponential_approximation(xs, ys):
    ys_ = list(map(log, ys))
    _, coefs = linear_approximation(xs, ys_)
    a = exp(coefs[0])
    b = coefs[1]
    return lambda xi: a*exp(b*xi), (a, b)


def logarithmic_approximation(xs, ys):
    xs_ = list(map(log, xs))
    _, coefs = linear_approximation(xs_, ys)
    a = coefs[0]
    b = coefs[1]
    return lambda xi: a + b*log(xi), (a, b)


def power_approximation(xs, ys):
    xs_ = list(map(log, xs))
    ys_ = list(map(log, ys))
    _, coefs = linear_approximation(xs_, ys_)
    a = exp(coefs[0])
    b = coefs[1]
    return lambda xi: a*xi**b, (a, b)
