# use nested for loops to iterate through the provided list, 
# which contains other lists, and print the respective sums
# of the inner lists, each on a separate line

lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

for inner_list in lst:
    sum_of_inner_list = 0

    for item in inner_list:
        sum_of_inner_list += item

    print(sum_of_inner_list)
