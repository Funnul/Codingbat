# Monkey_Trouble

# Monkeys A and B
# Smiles a_smile and b_smile
# if both smile, Trouble; if both not smile, Trouble

# # Attempt 1 - GOOD
# def monkey_trouble(a_smile, b_smile):
#     if a_smile == b_smile:
#         return True
#     else:
#         return False
#     return monkey_trouble

# Revised/shortened - BETTER


def monkey_trouble(a_smile, b_smile):
    return (a_smile == b_smile)

# The above can be shortened to:
  # return ((a_smile and b_smile) or (not a_smile and not b_smile))
  # Or this very short version (think about how this is the same as the above)
  # return (a_smile == b_smile)
