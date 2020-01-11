def divide(a, b, floor=True):
    """return true or floor division"""
    try:
        if floor:
            return a // b
        else:
            return a / b
    except TypeError:
        raise TypeError('unsupported operand type, use numbers of type int or float')


divide(2, 5, False)


def positional_keyword_argument(*args, **kwargs):
    try:
        print('args total value is: ', sum(list(args)))
        print('kwargs total value is: ', {'Total': sum([values for key, values in kwargs.items()])})
    except Exception:
        print('PASSED VALUES ARE NOT OF TYPE INT')

positional_keyword_argument(1, 2, 3, 4, a=1, b=9, c=3)
