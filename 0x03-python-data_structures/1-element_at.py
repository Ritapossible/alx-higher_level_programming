#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)

    get_length = len(my_list)

    if idx > get_length - 1:
        return (None)

    return(my_list[idx])
