# See practice question 5

def trim_list(lst, elements_to_trim):
    trimmed_list = []

    for idx in range(len(lst) - elements_to_trim):
        element = lst[idx]
        trimmed_list.append(element)

    return trimmed_list
