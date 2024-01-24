#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    if num_args != 3:
        print(num_args)
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(num_args)

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
