def last2(str):
    if len(str) < 2:
        return 0
    count = 0
    last2 = str[-2:]
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
            count = count + 1
    return count

# why does count and last 2 positioned in same hierarchy as for i
