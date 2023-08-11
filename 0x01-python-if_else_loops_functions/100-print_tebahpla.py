#!/usr/bin/python3

def print_reverse_alphabet():
    """Prints the ASCII alphabet in reverse order with alternating case."""
    for i in range(122, 96, -1):
        if i % 2 == 0:
            print("{:c}".format(i), end="")
        else:
            print("{:c}".format(i - 32), end="")

if __name__ == "__main__":
    print_reverse_alphabet()
