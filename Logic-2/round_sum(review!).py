def round_sum(a, b, c):
    def round10(num):
        # return (num+5)/10 * 10
        # (num+5)/10 * 10: why does this round to closest 10?
        # in most progamming languages, dividing an int with another int
        # means you throw away the remainder (i.e. 17 / 10 == 1, not 1.7)
        # (2+5)/10 = 0, not 0.7
        # (5+5)/10 = 1
        # (8+5)/10 = 1, not 1.3
        # alternative: int(round(num, -1))
        # int(floating number)
        # round(123.456, 1) == 120
        # round(123.456, -1) == 123.5
        # round(123.456, 2) == 100
        # round(123.456, -2) == 123.46

        # // for integer division
    return round10(a) + round10(b) + round10(c)

#     def round_sum(a, b, c):
#   return round10(a) + round10(b) + round10(c)
#
# def round10(num):
#   mod = num % 10
#   num -= mod
#   if mod >= 5: num += 10
#   return num
