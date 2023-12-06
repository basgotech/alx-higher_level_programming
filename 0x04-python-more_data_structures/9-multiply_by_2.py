#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir_to_deploy = a_dictionary.copy()
    list_keys_dep = list(new_dir_to_deploy.keys())
    for b in list_keys_dep:
        new_dir_to_deploy[b] *= 2
    return (new_dir_to_deploy)
