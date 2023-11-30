#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Extract all command line arguments, excluding the script name
    args = argv[1:]

    # Convert each argument to an integer and sum them up
    result = sum(int(arg) for arg in args)

    # Print the result followed by a new line
    print(result)
