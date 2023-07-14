def minmax(op, ls: list[float]):
    """
    Computes the smallest or largest value in a list of numbers based on provided operator
    :param op: operator > or <
    :return: smallest or largest value
    """

    if len(ls) == 0:
        raise ValueError("list must have at least one element")
    elif len(ls) == 1:
        return ls[0]
    else:
        if op(ls[0], minmax(op, ls[1:])):
            return ls[0]
        else:
            return minmax(op, ls[1:])


def inf(a, b):
    return a < b


def sup(a, b):
    return a > b


def main():
    print("LOW: ", minmax(inf, [0, 3, -2, 8, 5, 7, 0.4, 2]))
    print("HIGH: ", minmax(sup, [0, 3, -2, 8, 5, 7, 0.4, 2]))

main()