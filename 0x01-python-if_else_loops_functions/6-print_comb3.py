#!/usr/bin/python3

# Print all possible different combinations of two digits
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit == 8:
            print("{:d}{:d}".format(tens_digit, ones_digit))
        else:
            print("{:d}{:d}".format(tens_digit, ones_digit), end=', ')
