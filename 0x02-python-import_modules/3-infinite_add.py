#!/usr/bin/python3
def main(argv):
    add = 0
    for i in range(1, len(argv)):
        add += int(argv[i])
    print("{}".format(add))


if __name__ == "__main__":
    import sys
    main(sys.argv)
