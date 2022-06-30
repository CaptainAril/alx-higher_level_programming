#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv
    argv_len = len(argv)

    if (argv_len - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if operator not in ['+', '-', '_', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)

    if operator == '+':
        print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    if operator == '_':
        print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    if operator == '/':
        print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
