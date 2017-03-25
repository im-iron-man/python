class Tuple(tuple):

    """reconstruct __builtins__.tuple"""

    pass

def NamedTuple(name, data):

    """reconstruct collections.__namedtuple__"""

    # check data unique
    for x in data:
        if data.count(x) != 1:
            raise ValueError
    
    # attributes
    attrs = {}

    # __slots__
    attrs['__slots__'] = ()

    # __new__
    def tmp(cls, *args):
        if len(args) != len(data):
            raise TypeError
        return tuple.__new__(cls, args)

    attrs['__new__'] = tmp
        
    # data
    from operator import itemgetter
    for x in data:
        attrs[x] = property(itemgetter(data.index(x)))

    return type(name, (tuple, ), attrs)

