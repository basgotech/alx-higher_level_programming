#!/usr/bin/python3

""" used to add tow numbers """

def add_integer(a, b=98):
    """
    Adds two integers.

    This function takes two arguments, a and b, and adds them together. If either a or b is a float,
    they are first casted to integers before the addition. The default value for b is 98.

    Parameters:
    - a: An integer or float.
    - b: An integer or float (default is 98).

    Returns:
    An integer: the addition of a and b.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
