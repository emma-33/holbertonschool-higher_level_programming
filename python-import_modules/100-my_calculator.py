#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if operator == "+":
            result = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, result))
        elif operator == "-":
            result = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, result))
        elif operator == "*":
            result = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, result))
        elif operator == "/":
            result = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
