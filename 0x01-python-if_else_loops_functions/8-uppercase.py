#!/usr/bin/python3

def uppercase(s):
    """Prints a string in uppercase followed by a new line."""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
    print()

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    uppercase(input_string)
