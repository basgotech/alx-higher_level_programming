#!/usr/bin/python3

def uppercase(str):
    upper_text = ''
    for ch in str:
        if 'a' <= ch <= 'z':
            # Convert lowercase to uppercase using ASCII values
            upper_text += chr(ord(ch) - ord('a') + ord('A'))
        else:
            # Keep non-lowercase characters unchanged
            upper_text += ch
    return print("{}".format(upper_text))
