# See practice question 4

def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)

    set_intersection_length = 0
    for num in lst2:
        if num in lst1_set:
            set_intersection_length += 1
            lst1_set.remove(num)

    return set_intersection_length
