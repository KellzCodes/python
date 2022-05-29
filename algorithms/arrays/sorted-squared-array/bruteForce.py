def sortedSquaredArray(array):
    array2 = []
    for num in array:
        array2.append(num * num)
    array2.sort()
    return array2
