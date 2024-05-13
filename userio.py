import sys


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
    print(x)
    print(y)


def input_method():
    print("Enter the input file name or skip to enter data manually.")
    return get_input()


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
    return [], []
