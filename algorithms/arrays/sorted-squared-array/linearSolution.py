def sortedSquaredArray(array):
    # initialize array full of zeros 
    # with the same length of input array
    squares = [0 for _ in array]
    # set the pointers
    start = 0
    end = len(array) - 1

    # loop backwards through array
    for i in reversed(range(len(array))):
        # set bigger and smaller values
        small = array[start]
        big = array[end]

        # if absolute value of small value
        # is larger than big value, set the 
        # value of the current index of new
        # array to the square of the small 
        # number
        if abs(small) > abs(big):
            squares[i] = small * small
            start += 1
        # otherwise set the value of the current
        # index of new array to the square of the
        # big number
        else:
            squares[i] = big * big
            end -= 1
    # return the new array
    return squares
