def divide(a, b, floor=True):
    """return true or floor division"""
    try:
        if floor:
            return a // b
        else:
            return a / b
    except TypeError:
        return f'{a , b} is type {type(a)} and {type(b)} use numbers only'


def positional_keyword_argument(*args, **kwargs):
    try:
        print('args total value is: ',sum(list(args)))
        print('kwargs total value is: ',{'Total': sum([values for key, values in kwargs.items()])})
    except Exception:
        print('PASSED VALUES ARE NOT OF TYPE INT')


positional_keyword_argument(1, 2, 3, 4, a=1, b=9, c=3)