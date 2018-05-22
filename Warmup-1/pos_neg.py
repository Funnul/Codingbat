

# def pos_neg(a, b, negative):
#     if negative is True and ((a < 0) and (b < 0)):
#         return True
#     elif negative is False and ((a < 0 and b > 0) or (a > 0 and b < 0)):
#         return True
#     else:
#         return False
#     return pos_neg

# revised (shorter version)


def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))
