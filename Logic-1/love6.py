def love6(a, b):
    if (a == 6) or (b == 6) or (a + b == 6) or (a - b == 6) or (b - a == 6):
        return True
    return False

    # return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6
    # DIFFERENCE use abs (removes ± sign)
