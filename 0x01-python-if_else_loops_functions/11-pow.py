#!/usr/bin/python3

def pow(a, b):
    """Computes a to the power of b and returns the result."""
    result = 1
    for _ in range(b):
        result *= a
    return result

if __name__ == "__main__":
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    power_result = pow(base, exponent)
    print(f"{base} raised to the power of {exponent} is {power_result}.")
