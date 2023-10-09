#!/usr/bin/python3
def multiple_returns(sentence):
    len_sent = len(sentence)

    if (len_sent == 0):
        new_tuple = (len_sent, None)
    else:
        new_tuple = (len_sent, sentence[0])

    return (new_tuple)
