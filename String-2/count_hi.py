def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            count += 1
    return count

    # for loop to go through each i
    # str[i:i+2] to go through each 2 letters
