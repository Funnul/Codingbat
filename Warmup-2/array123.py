def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

    # range(len(nums)-2) to use i+1 and i+2 in loop
    # use nums[i] instead of i
