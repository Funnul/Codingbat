# def lucky_sum(a, b, c):
#     sum = a + b + c
#     list = [a, b, c]
#     for i in list:
#         if list[i] == 13:
#             sum = sum - list[i:]
#         return sum

    sum = 0
    list = [a, b, c, 13]
    # Index for 13, then only sum up everything to the left
    for n in list[:list.index(13)]:
        sum += n
    return sum
