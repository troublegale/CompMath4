def solve_system(a, b):
    n = len(b)
    if n == 2:
        return solve2(a, b)
    if n == 3:
        return solve3(a, b)
    if n == 4:
        return solve4(a, b)


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def solve2(a, b):
    n = 2
    d = det2(a)
    d1 = det2([[b[r], a[r][1]] for r in range(n)])
    d2 = det2([[a[r][0], b[r]] for r in range(n)])
    x1 = d1 / d
    x2 = d2 / d
    return x1, x2


def det3(a):
    pos = (a[0][0] * a[1][1] * a[2][2] +
           a[0][1] * a[1][2] * a[2][0] +
           a[0][2] * a[1][0] * a[2][1])
    neg = (a[0][2] * a[1][1] * a[2][0] +
           a[0][1] * a[1][0] * a[2][2] +
           a[0][0] * a[1][2] * a[2][1])
    return pos - neg


def solve3(a, b):
    d = det3(a)
    d1 = det3([[b[i], a[i][1], a[i][2]] for i in range(3)])
    d2 = det3([[a[i][0], b[i], a[i][2]] for i in range(3)])
    d3 = det3([[a[i][0], a[i][1], b[i]] for i in range(3)])
    x1 = d1 / d
    x2 = d2 / d
    x3 = d3 / d
    return x1, x2, x3


def det4(a):
    n = 4
    sign = 1
    r = 0
    res = 0
    for c in range(n):
        a_ = [[a[r_][c_] for c_ in range(n) if c_ != c]
              for r_ in range(n) if r_ != r]
        res += sign * a[r][c] * det3(a_)
        sign *= -1
    return res


def solve4(a, b):
    d = det4(a)
    d1 = det4([[b[r], a[r][1], a[r][2], a[r][3]] for r in range(4)])
    d2 = det4([[a[r][0], b[r], a[r][2], a[r][3]] for r in range(4)])
    d3 = det4([[a[r][0], a[r][1], b[r], a[r][3]] for r in range(4)])
    d4 = det4([[a[r][0], a[r][1], a[r][2], b[r]] for r in range(4)])
    x1 = d1 / d
    x2 = d2 / d
    x3 = d3 / d
    x4 = d4 / d
    return x1, x2, x3, x4
