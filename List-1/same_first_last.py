def same_first_last(nums):
    for i in nums:
        if len(nums) >= 1 and (nums[0] == nums[-1]):
            return True
    return False
