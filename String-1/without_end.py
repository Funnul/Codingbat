def without_end(str):
    # if len(str) <= 2:
    #     return str[:]
    # why not needed? return str[1:-1] takes into account strings <= 2
    return str[1:-1]
    # remember last digit is not inclusive
