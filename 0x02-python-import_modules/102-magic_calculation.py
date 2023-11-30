#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        mgic = add(a, b)
        for i in range(4, 6):
            mgic = add(mgic, i)
        return (mgic)
    else:
        return (sub(a, b))
