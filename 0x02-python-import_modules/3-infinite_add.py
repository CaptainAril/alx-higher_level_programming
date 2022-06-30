#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv_len = len(argv)
    sum = 0
    if argv_len - 1 == 0:
        print(f"{sum:d}")
    else:
        for i in range(1, argv_len):
            sum += int(argv[i])
        print(f"{sum:d}")
