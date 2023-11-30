#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    numArgs = len(argv) - 1  # Subtract 1 for the script name
    arg_plural = "arguments" if numArgs != 1 else "argument"
    sep = ":" if numArgs > 0 else "."

    print("{} {}{}{}".format(numArgs, arg_plural, sep, "" if numArgs > 0 else ""))

    for i in range(1, numArgs + 1):
        print("{}: {}".format(i, argv[i]))
