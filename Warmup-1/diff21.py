# Diff 21


def diff21(n):
    if n > 21:
        return 2 * (n - 21)
    elif n <= 21:
        return 21 - n
    return diff21
