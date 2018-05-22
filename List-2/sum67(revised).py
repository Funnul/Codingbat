def sum67(nums):
    # Make a copy
    nums = nums[:]
    while 6 in nums:
        # use nums.index to find 6 and 7
        i = nums.index(6)
        # why (7, i)? (the first 7 after i)
        j = nums.index(7, i)
        del nums[i:j+1]
    return sum(nums)
