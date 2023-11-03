#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    plus = calc.add(a, b)
    minus = calc.sub(a, b)
    divide = calc.div(a, b)
    multiply = calc.mul(a, b)
    print("{} + {} = {}".format(a, b, plus))
    print("{} - {} = {}".format(a, b, minus))
    print("{} * {} = {}".format(a, b, multiply))
    print("{} / {} = {}".format(a, b, divide))
