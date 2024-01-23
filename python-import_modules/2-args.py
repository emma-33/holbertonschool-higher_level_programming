#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_of_args = len(sys.argv) - 1

    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_of_args))

    if num_of_args >= 1:
        for i in range(num_of_args):
            print("{}: {}".format(i+1, sys.argv[i + 1]))
