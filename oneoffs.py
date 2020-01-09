def divide(a, b, floor=True):
    """return true or floor division"""
    try:
        if floor:
            return a // b
        else:
            return a / b
    except TypeError:
        return f'{a , b} is type {type(a)} and {type(b)} use numbers only'

