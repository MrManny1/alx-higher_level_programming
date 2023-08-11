#!/usr/bin/python3

def add(a, b):
    """Adds two integers and returns the result."""
    result = a + b
    return result

if __name__ == "__main__":
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    sum_result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}.")

