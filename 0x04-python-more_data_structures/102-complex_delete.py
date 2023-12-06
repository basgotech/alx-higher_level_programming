#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys_dep = list(a_dictionary.keys())
    for value_dic_dep in list_keys_dep:
        if value == a_dictionary.get(value_dic_dep):
            del a_dictionary[value_dic_dep]
    return (a_dictionary)
