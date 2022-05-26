def isValidSubsequence(array, sequence):
    # create pointers for array index and sequence index
    arrIdx = 0
    seqIdx = 0
    # set array pointer and sequence pointer to beginning of the arrays
    while arrIdx < len(array) and seqIdx < len(sequence):
        # if value at array index is equal to value at sequence index
        # move sequence 
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        # move array index
        arrIdx += 1
    # will return true if the sequence index went through
    # the entire sequence array
    # will return false otherwise
    return seqIdx == len(sequence)
