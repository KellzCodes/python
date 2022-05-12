# Write a function that takes in a list of
# integers and returns a new list containing
# all of the odd numbers of the original list,
# in the order in which they appear. You can 
# assume that the list parameter will only 
# contain integers

def find_all_odds(lst):
    # Write your code here.
    new_list = []
    for num in lst:
        if num % 2 == 1:
            new_list.append(num)
            
    return new_list
