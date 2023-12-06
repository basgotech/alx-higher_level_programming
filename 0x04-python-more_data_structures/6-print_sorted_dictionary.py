#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord_deploy = list(a_dictionary.keys())
    list_ord_deploy.sort()
    for b in list_ord_deploy:
        print("{}: {}".format(b, a_dictionary.get(b)))
