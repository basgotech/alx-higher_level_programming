#!/usr/bin/python3

def magic_calculation(a, b):
    
    from magic_calculation_102 import add, sub

    if a < b:
        magic = add(a, b)
        for b in range(4, 6):
            magic = add(magic, b)
        return (magic)

    else:
        return(sub(a, b))
