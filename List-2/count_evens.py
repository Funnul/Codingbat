def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count = count + 1
    return count
