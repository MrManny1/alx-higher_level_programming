#!/usr/bin/python3

def print_last_digit(number):
    """Prints and returns the last digit of a number."""
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    last_digit = print_last_digit(num)

