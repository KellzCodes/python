# See practice question 6

def running_sums(numbers):
    sums = []

    current_sum = 0
    for number in numbers:
        current_sum += number
        sums.append(current_sum)

    return sums
