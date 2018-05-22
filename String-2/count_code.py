def count_code(str):
    count = 0
    # len(str)-3 to account for [i+3]
    # because len(str)-1 string index out of reach
    for i in range(len(str)-3):
        # for i in range(len(str)-1):
        if (str[i:i+2] == "co") and (str[i+3] == "e"):
            count += 1
    return count
