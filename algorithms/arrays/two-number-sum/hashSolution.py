def twoNumberSum(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current = array[left] + array[right]
        if current == target:
            return [array[left], array[right]]
        elif current < target:
            left += 1
        elif current > target:
            right -= 1
    return []
