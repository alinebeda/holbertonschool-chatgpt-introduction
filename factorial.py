#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    try:
        while n > 1:
            result *= n
            n -= 1
        return result
    except KeyboardInterrupt:
        print("\n^CTraceback (most recent call last):")
        print("  File \"" + sys.argv[0] + "\", line 9, in <module>")
        print("    factorial(int(sys.argv[1]))")
        print("  File \"" + sys.argv[0] + "\", line 5, in factorial")
        print("    while n > 1:")
        print("KeyboardInterrupt")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Please enter a valid integer number.")
        sys.exit(1)

