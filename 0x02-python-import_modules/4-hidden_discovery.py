#!/usr/bin/python3
def main():
    for name in dir(hide):
        if not name[0] == "-" and name[1] == "-":
            print(name)


if __name__ == "__main__":
    import hidden_4 as hide
    main()
