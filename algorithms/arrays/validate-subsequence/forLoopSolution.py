# Create pointer for sequence
    seqIdx = 0
    # iterate through array
    for value in array:
        # break out the loop if sequence index 
        # reaches the end of the sequence
        if seqIdx == len(sequence):
            break
        # move the sequence index if the sequence value
        # matches the value in the array
        if sequence[seqIdx] == value:
            seqIdx += 1
    # will return true if the sequence index went through
    # the entire sequence array
    # will return false otherwise
    return seqIdx == len(sequence)
