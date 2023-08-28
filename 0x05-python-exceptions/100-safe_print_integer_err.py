#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer using the "{:d}" format.

    If a TypeError or ValueError occurs, an error message is printed
    to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if printing succeeds, False if an exception occurs.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
