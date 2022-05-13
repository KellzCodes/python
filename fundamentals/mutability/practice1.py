# See practice question

def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        element = lst[idx]

        if element == target:
            lst[idx] = swap_value
