# def array_front9(nums):
#     for i in nums[0:4]:
#         if i == 9:
#             return True
#         else:
#             return False
# This function only works if 9=nums[0]
# Put "return false" at a higher hierarchy


def array_front9(nums):
    for i in nums[0:4]:
        if i == 9:
            return True
    return False
