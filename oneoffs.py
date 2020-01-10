def divide(a, b, floor=True):
    """return true or floor division"""
    try:
        if floor:
            return a // b
        else:
            return a / b
    except TypeError:
        raise TypeError('unsupported operand type, use numbers of type int or float')


divide('a', 5, False)