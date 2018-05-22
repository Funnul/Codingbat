# def no_teen_sum(a, b, c):
#     list = [a, b, c]
#     def fix_teen(n):
#         return False if 13 >= n >= 19 or n in [15, 16] else True
#     for n in list:
#         sum += n if True else False


def no_teen_sum(a, b, c):
    def fix_teen(n):
        return n if n not in [13, 14, 17, 18, 19] else 0
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
    # So elegant!
    # Tips: use [13, 14, 15...]
    # Tips: Use helper function to streamline sum
