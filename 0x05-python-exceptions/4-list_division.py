#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_div = []

    for x in range(list_length):
        try:
            div_res = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            div_res = 0
        except ZeroDivisionError:
            print("division by 0")
            div_res = 0
        except IndexError:
            print("out of range")
            div_res = 0
        finally:
            result_div.append(div_res)

    return result_div
