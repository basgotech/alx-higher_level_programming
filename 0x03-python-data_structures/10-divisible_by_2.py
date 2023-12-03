#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lists = []
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            new_lists.append(True)
        else:
            new_lists.append(False)
    return new_lists
