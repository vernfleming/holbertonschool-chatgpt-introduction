#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer.

    Parameters:
    n (int): The number to compute the factorial of. Must be a non-negative integer.

    Returns:
    int: The factorial of the input number `n`.
         If n is 0, returns 1 as 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the first command-line argument, convert to int, and compute the factorial
f = factorial(int(sys.argv[1]))
print(f)
