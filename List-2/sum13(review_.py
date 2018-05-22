def sum13(nums):
    sum = 0
    i = 0
    # Think of while as a train going through each element
    while i < len(nums):
        if nums[i] == 13:
            # Numbers that come immediately after don't count +1, +1 again
            i += 1
        else:
            sum += nums[i]
        # move onto next element
        i += 1
    return sum

    # a += b means a = a + b
    # a += b basically adds b on top

# def sum13(nums):
#
#     total = 0
#     i = 0
#
#     while i < len(nums):
#         if nums[i] == 13:
#             i += 2
#             continue
#         total += nums[i]
#         i += 1
#
#     return total
