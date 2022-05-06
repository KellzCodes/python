# use a single for loop to iterate through the provided list,
# and print the elements that are both divisible by 2 and 
# located at an odd index, each on a separate line.

lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

for idx in range(len(lst)):
    item = lst[idx]

    if item % 2 == 0 and idx % 2 != 0:
        print(item)
