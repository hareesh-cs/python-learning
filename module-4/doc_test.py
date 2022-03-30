def mul(a, b):
    """
    >>> mul(3,4)
    12
    >>> mul('b',6)
    'bbbbbb'
    """
    return a * b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
