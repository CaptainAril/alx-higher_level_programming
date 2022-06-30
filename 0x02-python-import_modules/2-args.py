#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv_len = len(argv)
    if (argv_len - 1) == 0:
        print("{} arguments.".format(argv_len - 1))
    elif (argv_len - 1) == 1:
        print("{} argument:".format(argv_len - 1))
    else:
        print("{} arguments:".format(argv_len - 1))
    for i in range(1, argv_len):
        print("{:d}: {}".format(i, argv[i]))
