from numpy import sqrt


def standard_deviation(x, y, phi):
    n = len(x)
    return sqrt(sum(((phi(xi) - yi) ** 2 for xi, yi in zip(x, y))) / n)


def pearson_correlation(x, y):
    n = len(x)
    avg_x = sum(x) / n
    avg_y = sum(y) / n
    return (sum((x - avg_x) * (y - avg_y) for x, y in zip(x, y)) /
            sqrt(sum((x - avg_x) ** 2 for x in x) * sum((y - avg_y) ** 2 for y in y)))
