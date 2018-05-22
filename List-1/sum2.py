def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return sum(nums)
    else:
        return sum(nums[:2])
