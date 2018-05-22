# def make_bricks(small, big, goal):
#     s = small * 1
#     b = big * 5
#     if (b + s >= goal):
#         return True
#     else:
#         return False


def make_bricks(small, big, goal):
    # Distance bigs cover? Goal - lowest number of bigs needed * 5cm = Remaining distance
    goal = goal - 5 * min(big, goal/5)
    # Enough smalls to cover? Remaining distance - smalls = 0 or lower
    return (goal - small) <= 0
