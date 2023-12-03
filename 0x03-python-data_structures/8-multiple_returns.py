#!/usr/bin/python3
def multiple_returns(sentence):
    my_sent = ()
    if len(sentence) == 0:
        my_sent = 0, "None"
    else:
        my_sent = len(sentence), sentence[0]
    return my_sent
