from os import access, R_OK, path


def check_file_exists(filename):
    return path.isfile(filename)


def check_file_accessible(filename):
    return access(filename, R_OK)


def read_data_from_file(filename):
    x, y = [], []
    with open(filename, 'r') as file:
        while True:
            s = file.readline().strip().replace(',', '.')
            if not s:
                break
            try:
                xi, yi = map(lambda t: float(t), s.split())
                x.append(xi)
                y.append(yi)
            except ValueError:
                return 0
            if len(x) == 12:
                return x, y
    if len(x) < 8:
        return 0
    return x, y
