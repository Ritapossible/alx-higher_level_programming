#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    oper = sys.argv[2]
    if oper != '+' and oper != '-' and oper != '*' and oper != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if oper == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif oper == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif oper == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
