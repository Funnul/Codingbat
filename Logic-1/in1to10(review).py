# def in1to10(n, outside_mode):
#     if outside_mode and (n <= 1 or n >= 10):
#         return True
#     elif not outside_mode and (1 <= n <= 10):
#         return True
#     return False
# in1to10(9, True) → False does not work>
# logic: because forgot to add "not outside_mode"


def in1to10(n, outside_mode):
    if n == 1 or n == 10:
        return True
    return (n in range(1, 11)) ^ outside_mode

    # what is ^?
