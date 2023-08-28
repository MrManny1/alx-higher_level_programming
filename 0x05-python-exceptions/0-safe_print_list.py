#!/usr/bin/python3

def unique_safe_print_list(my_list=[], x=0):
    """Print up to x elements of a list, handling errors gracefully.

    Args:
        my_list (list): The list to print elements from.
        x (int): The maximum number of elements from my_list to print.

    Returns:
        The actual number of elements successfully printed.
    """
    num_printed = 0
    for i in range(x):
        try:
            print("Item: {}".format(my_list[i]), end="")
            num_printed += 1
        except IndexError:
            print("\nReached the end of the list.")
            break
    print("\nPrinted {} elements.".format(num_printed))
    return num_printed

