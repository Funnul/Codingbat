# def has22(nums):
#     while 2 in nums:
#         a = nums.index(2)
#         if nums[a] == nums[a+1]:
#             return True
#         return False


def has22(nums):
    # use range(0, len) instead of nums to make sure it loops
    for i in range(0, len(nums)):
        # why i+2? because not inclusive!
        if nums[i:i+2] == [2, 2]:
            return True
    return False
