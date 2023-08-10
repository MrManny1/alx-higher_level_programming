#!/usr/bin/python3

def islower(c):
    """Check if a character is lowercase."""
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False

if __name__ == "__main__":
    char = input("Enter a character: ")
    if len(char) == 1:
        if islower(char):
            print(f"{char} is lowercase.")
        else:
            print(f"{char} is not lowercase.")
    else:
        print("Please enter a single character.")
