#!/usr/bin/python3

def islower(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

# Test cases
print(islower('a'))  # Output: True
print(islower('Z'))  # Output: False
print(islower('7'))  # Output: False
