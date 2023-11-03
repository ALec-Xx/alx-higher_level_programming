#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    len_args = len(argv) - 1
    if len_args == 0:
        print("0 arguments.")
    elif len_args == 1:
        print("1 argument:\n1:", argv[1])
    else:
        print("{} arguments:".format(len_args))
        for item in range (1, len_args + 1):
            print("{}: {}".format(item, argv[item]))
