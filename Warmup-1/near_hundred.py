#
# # Failed
# def near_hundred(a):
#     return (a is range(abs(190), abs(210)) or a is range(abs(90), abs(110)))

# Reattempt


def near_hundred(a):
    return ((abs(100 - a) <= 10) or (abs(200 - a) <= 10))

    
