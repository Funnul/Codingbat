# Parrot Monkey_Trouble
# Hour = current hour expresed 0...23
# if talk <7 or >20, return Trouble

# Attempt 1
# def parrot_trouble(talking, hour):
#     if not talking:
#         return False
#     elif hour < 7:
#         return True
#     elif hour > 20:
#         return True
#     else:
#         return False
#     return parrot_trouble

# Revised


def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))

    # Lesson: and (*) binds tighter than or (+)
