#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result_grapper = a / b
    except ZeroDivisionError:
        result_grapper = None
    finally:
        print("Inside result: {}".format(result_grapper))
        return result_grapper
