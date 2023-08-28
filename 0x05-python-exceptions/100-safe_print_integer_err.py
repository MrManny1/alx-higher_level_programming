#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer using "{:d}".format().

    If a TypeError or ValueError occurs, an error message is printed to
    standard error.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if printing is successful, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception:", e, file=sys.stderr)
        return False

# Example usage
value = 42
result = safe_print_integer_err(value)
print("Printing successful:", result)
