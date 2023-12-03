#!/usr/bin/env python3
def no_c(my_string):
    str_list = list(my_string)
    for i in range(len(str_list)):
     if str_list[i] == 'c' or str_list[i] == 'C':
        str_list[i] = ''
    result_str = ''.join(str_list)
    return result_str
