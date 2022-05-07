# Use a while loop to print the squares of the numbers: 
# 1, 3, 6, 10, 15, and 21

lis = [1, 3, 6, 10, 15, 21]

result = 0
i = 0

while i < len(lis):
    num = lis[i]
    result = num * num
    i += 1

    print(result)
