class IntAdd(int):

    """
    >>> IntAdd(1)(2)
    3
    >>> IntAdd(1)(2)(3)
    6
    """

    def __call__(self, v):
        return IntAdd(self+v)

class FloatAdd(float):
    
    """
    >>> FloatAdd(1)(2)
    3.0
    >>> FloatAdd(1)(2)(3)
    6.0
    """
    
    def __call__(self, v):
        return FloatAdd(self+v)

class IntPlus(int):

    """
    >>> IntPlus(1)(2)
    2
    >>> IntPlus(1)(2)(3)
    6
    """

    def __call__(self, v):
        return IntPlus(self*v)

class FloatPlus(float):

    """
    >>> FloatPlus(1)(2)
    2.0
    >>> FloatPlus(1)(2)(3)
    6.0
    """

    def __call__(self, v):
        return FloatPlus(self*v)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
