def twoNumberSum(array, target):
    nums = {}
    for num in array:
        match = target - num
        if match in nums:
            return [match, num]
        else:
            nums[num] = True
    return []
