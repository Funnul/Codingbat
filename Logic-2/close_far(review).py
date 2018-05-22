# def close_far(a, b, c):
#     if (abs(b-a) <= 1 and abs(c-a) >= 2) or (abs(c-a) <= 1 and abs(b-a) >= 2):
#         return True
#     return False
#     # Failed because ask yourself: what if abs(b-a) >=
#     # Needs more abs as below


# def close_far(a, b, c):
#     if (abs(abs(b)-abs(a))) <= 1 and (abs(abs(c)-abs(a))) >= 2 or (abs(abs(c)-abs(a))) <= 1 and (abs(abs(b)-abs(a))) >= 2:
#         return True
#     return False

def close_far(a, b, c):
    return (abs(abs(b)-abs(c)) >= 2) and \
        ((abs(abs(b)-abs(a)) <= 1 and abs(abs(c)-abs(a)) >= 2)
         or (abs(abs(c)-abs(a)) <= 1 and abs(abs(b)-abs(a)) >= 2))

    # \ is a line break
    #
