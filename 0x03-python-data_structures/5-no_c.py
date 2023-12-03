#!/usr/bin/env python3
def no_c(my_string):
    fil_c = [char for char in my_string if char.lower() not in ('c', 'C')]
    result_str = ''.join(fil_c)
    return result_str
