# use a single for loop to iterate through the provided
# list of numbers, and for each number, print the sum
# of the number and the one directly to its right. In
# other words, print lst[i] + lst[i + 1]. Since the 
# last number in the list has no number to the right 
# of it, you should simply skip it.

lst = [-2, 0, 4, 5, 1, 2]

for idx in range(len(lst) - 1):
    current_item = lst[idx]
    next_item = lst[idx + 1]

    sum_of_items = current_item + next_item
    print(sum_of_items)
