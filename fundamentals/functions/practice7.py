# See practice question 4

def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)

    set_intersection_length = 0
    for num in lst1_set:
        if num in lst2_set:
            set_intersection_length += 1

    return set_intersection_length
