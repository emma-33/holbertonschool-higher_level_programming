#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    num_args = len(argv) - 1

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if operator == "+":
            print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
        elif operator == "*":
            print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
        elif operator == "/":
            print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
