def near_ten(num):


"""
  Given a non-negative number "num", return True if num is within 2 of a
  multiple of 10. Note: (a % b) is the remainder of dividing a by b,
  so (7 % 5) is 2.
"""
#within = num - (num+2)/10*10
# return within in range(-2,3)

# Within = multiple of 10 from the num
# num%((num/10)*10) means 22 (2.2)
# num % ((num/10)*10) is the same as n % 10
    within = n % 10
    # within = num % ((num/10)*10) if num >= 10 else num
    # Check if within is within 2
    return within in [8, 9, 0, 1, 2]
