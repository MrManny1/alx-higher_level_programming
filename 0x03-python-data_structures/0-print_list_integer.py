#!/usr/bin/pythong

def print_list_integer(my_list=[]):
    """Print all integers of the list."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
