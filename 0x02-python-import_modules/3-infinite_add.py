#!/usr/bin/python3

def main():
    """Print the sum of all command-line arguments."""
    import sys

    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print("Sum:", total)

if __name__ == "__main__":
    main()

