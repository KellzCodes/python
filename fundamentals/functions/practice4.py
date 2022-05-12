# Write a function that takes in a list of strings 
# and returns a new list containing the lengths of 
# the strings, in their relevant order. You can 
# assume that "strings" will only contain strings

def string_lengths(strings):
    # Write your code here.
    new_list = []
    for string in strings:
        new_list.append(len(string))
    return new_list
