from math import inf
import sys
from approximation import *
from file import *
from stats import *
from tabulate import tabulate


def get_input():
    try:
        return input("$ ").strip().replace(",", ".")
    except (EOFError, KeyboardInterrupt):
        close_application_appropriately()


def close_application_appropriately():
    print("\nClosing application...")
    exit()


def launch():
    hello = "Computational Mathematics Lab 4: Function approximation"
    print("-" * len(hello))
    print(hello)
    print("-" * len(hello))
    print()
    start()
    sys.stdout = sys.__stdout__
    close_application_appropriately()


def start():
    in_method = input_method()
    if in_method:
        x, y = get_data_file(in_method)
    else:
        x, y = get_data_manual()
    out_method = output_method()
    if out_method:
        with open(out_method, 'w') as out:
            sys.stdout = out
            approximate(x, y)
    else:
        approximate(x, y)


def approximate(x, y):
    print()
    approximations = {"linear": do_linear_approximation(x, y),
                      "quadratic": do_quadratic_approximation(x, y),
                      "cubic": do_cubic_approximation(x, y)}
    if all(map(lambda t: t > 0, x)):
        approximations["logarithmic"] = do_logarithmic_approximation(x, y)
        if all(map(lambda t: t > 0, y)):
            approximations["exponential"] = do_exponential_approximation(x, y)
            approximations["power"] = do_power_approximation(x, y)
    elif all(map(lambda t: t > 0, y)):
        approximations["exponential"] = do_exponential_approximation(x, y)
    best = "amogus"
    sd = inf
    for name in approximations.keys():
        if approximations[name] < sd:
            best = name
            sd = approximations[name]
    print(f"Best approximation by standard deviation: {best}")


def do_linear_approximation(x, y):
    phi, coefs = linear_approximation(x, y)
    print("Linear approximation:")
    print(f"phi(x) = {coefs[0]} " + ('+' if coefs[1] >= 0 else '-') + f" {abs(coefs[1])}x")
    print_approximation_results(phi, x, y)
    pearson = pearson_correlation(x, y)
    if abs(pearson) == 1:
        pearson_conclusion = "strict linear dependence"
    elif abs(pearson) >= 0.9:
        pearson_conclusion = "very high linear dependence"
    elif abs(pearson) >= 0.7:
        pearson_conclusion = "high linear dependence"
    elif abs(pearson) >= 0.5:
        pearson_conclusion = "noticeable linear dependence"
    elif abs(pearson) >= 0.3:
        pearson_conclusion = "moderate linear dependence"
    elif abs(pearson) != 0:
        pearson_conclusion = "weak linear dependence"
    else:
        pearson_conclusion = "no linear dependence"
    print(f"Pearson's correlation coefficient: {pearson}, {pearson_conclusion}")
    print()
    return standard_deviation(x, y, phi)


def do_quadratic_approximation(x, y):
    phi, coefs = quadratic_approximation(x, y)
    print("Quadratic approximation:")
    print(f"phi(x) = {coefs[0]} " + ('+' if coefs[1] >= 0 else '-') +
          f" {abs(coefs[1])}x " + ('+' if coefs[2] >= 0 else '-') + f" {abs(coefs[2])}x^2")
    print_approximation_results(phi, x, y)
    print()
    return standard_deviation(x, y, phi)


def do_cubic_approximation(x, y):
    phi, coefs = cubic_approximation(x, y)
    print("Cubic approximation:")
    print(f"phi(x) = {coefs[0]} " + ('+' if coefs[1] >= 0 else '-') +
          f" {abs(coefs[1])}x " + ('+' if coefs[2] >= 0 else '-') + f" {abs(coefs[2])}x^2 " +
          ('+' if coefs[3] >= 0 else '-') + f" {abs(coefs[3])}x^3")
    print_approximation_results(phi, x, y)
    print()
    return standard_deviation(x, y, phi)


def do_logarithmic_approximation(x, y):
    phi, coefs = logarithmic_approximation(x, y)
    print("Logarithmic approximation:")
    print(f"phi(x) = {coefs[0]}ln(x) " + ('+' if coefs[1] >= 0 else '-') + f" {abs(coefs[1])}")
    print_approximation_results(phi, x, y)
    print()
    return standard_deviation(x, y, phi)


def do_exponential_approximation(x, y):
    phi, coefs = exponential_approximation(x, y)
    print("Exponential approximation:")
    print(f"phi(x) = {coefs[0]}e^({coefs[1]}x)")
    print_approximation_results(phi, x, y)
    print()
    return standard_deviation(x, y, phi)


def do_power_approximation(x, y):
    phi, coefs = power_approximation(x, y)
    print("Power approximation:")
    print(f"phi(x) = {coefs[0]}x^{coefs[1]}")
    print_approximation_results(phi, x, y)
    print()
    return standard_deviation(x, y, phi)


def print_approximation_results(phi, x, y):
    data = [['xi', 'yi', 'phi(xi)', 'ei']]
    for i in range(len(x)):
        data.append([x[i], y[i], phi(x[i]), phi(x[i]) - y[i]])
    print(tabulate(data))
    sd = standard_deviation(x, y, phi)
    print(f"Standard deviation: {sd}")
    dc = determination_coefficient(x, y, phi)
    print(f"Determination coefficient: {dc}")


def input_method():
    print("Enter the input file name or skip to enter data manually.")
    while True:
        ans = get_input()
        if (not ans) or (check_file_exists(ans) and check_file_accessible(ans)):
            return ans
        else:
            print(f"File '{ans}' does not exist or couldn't access file '{ans}'.")


def output_method():
    print("Enter the output file name or skip to receive output in console.")
    return get_input()


def get_data_manual():
    print("Enter the number of points (8 to 12).")
    x, y = [], []
    while True:
        try:
            n = int(get_input())
            if n < 8:
                print("Number of points has to be at least 8.")
                continue
            if n > 12:
                print("Number of points can't be greater than 12.")
                continue
            x, y = get_points(n)
            break
        except ValueError:
            print("Please, enter a valid number.")
            continue
    return x, y


def get_points(n):
    i = 0
    x, y = [], []
    print(f"Enter {n} pairs of x and y.")
    while True:
        try:
            xi, yi = map(lambda t: float(t), get_input().split())
            if xi in x:
                ind = x.index(xi)
                print(f"This x has already been entered and corresponds to y = {y[ind]}")
                continue
            x.append(xi)
            y.append(yi)
            i += 1
            if i == n:
                break
        except ValueError:
            print("Please, enter a valid pair of numbers.")
            continue
    return x, y


def get_data_file(name):
    x, y = read_data_from_file(name)
    if x:
        return x, y
    else:
        print(f"File '{name}' is invalid.")
        close_application_appropriately()
