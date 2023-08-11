#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1
    args_word = "argument" if num_args == 1 else "arguments"

    print(f"Number of {args_word}: {num_args}")

    if num_args > 0:
        print(":")
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")
    else:
        print(".")
