#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count_len = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count_len += 1
        print()
        return count_len
    except IndexError:
        print()
        return count_len
