

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[len(str)-1] + str[1:-1] + str[0]
    return front_back

# len(str)-1 is last letter, 1:-1 is range from 2nd to 2nd last
# because 1:-1 range is non-inclusive of -1
