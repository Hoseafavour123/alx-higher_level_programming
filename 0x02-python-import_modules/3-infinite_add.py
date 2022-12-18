#!/usr/bin/python3

if __name__ == "__main__":
    """Add all arguments passed."""

    import sys

    total = 0
    count = len(sys.argv) - 1

    for i in range(count):
        i = int(sys.argv[i + 1])
        total += i
    print("{}".format(total))
