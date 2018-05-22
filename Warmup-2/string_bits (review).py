# def string_bits(str):
#     n == str[n]
#     if n % 2 == 0:
#         str.replace([str[n], "")
#     return string_bits


# def string_bits(str):
#     for i in range(len(str)):
#         if i % 2 == 0:
#             str.replace(i, "")
#     return string_bits

def string_bits(str):
    # define result as "blank"
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            # final result is "blank" plus "even words only (or odd if 0:-1)"
            result = result + str[i]
    return result
