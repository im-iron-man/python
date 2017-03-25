class Dict(object):

    """reconstruct __builtins__.dict"""

    __kv = {}
    
    def __init__(self, *args, **kwargs):
        self.__kv = dict(*args, **kwargs)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError(key)
        return self.__kv.__getitem__(key)

    def __setitem__(self, key, value):
        self.__kv.__setitem__(key, value)

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        self.__kv.__delitem__(key)
        
    def keys(self):
        return self.__kv.keys()

    def values(self):
        return self.__kv.values()

    def items(self):
        return self.__kv.items()

    def update(self, other):
        self.__kv.update(other)

    def pop(self, key):
        if key not in self:
            raise KeyError(key)
        return self.__kv.pop(key)

    def __iter__(self):
        return self.__kv.__iter__()

    def __len__(self):
        return self.__kv.__len__()
    
    def __str__(self):
        return self.__kv.__str__()

    __repr__ = __str__
    
class DefaultDict(Dict):

    """reconstruct collections.defaultdict"""
    
    def __init__(self, obj):
        self.obj = obj
        
    def __getitem__(self, key):
        if key not in self:
            return self.obj
        return super(DefaultDict, self).__getitem__(key)

class OrderedDict(Dict):

    """reconstruct collections.OrderedDict"""

    __kpool, __vpool = [], []
    
    def __init__(self, *args, **kwargs):
        super(OrderedDict, self).__init__(*args, **kwargs)
        self.__kpool.extend(super(OrderedDict, self).keys())
        self.__vpool.extend(super(OrderedDict, self).values())
        
    def __setitem__(self, key, value):
        super(OrderedDict, self).__setitem__(key, value)
        if key in self.__kpool:
            index = self.__kpool.index(key)
            self.__kpool.pop(index)
            self.__vpool.pop(index)
        self.__kpool.append(key)
        self.__vpool.append(value)
        
    def __delitem__(self, key):
        super(OrderedDict, self).__delitem__(key)
        index = self.__kpool.index(key)
        self.__kpool.__delitem__(index)
        self.__vpool.__delitem__(index)
        
    def keys(self):
        return self.__kpool

    def values(self):
        return self.__vpool

    def items(self):
        return zip(self.__kpool, self.__vpool)

    def update(self, other):
        for key in other:
            self.__setitem__(key, other.__getitem__(key))

    def pop(self, key):
        value = super(OrderedDict, self).pop(key)
        index = self.__kpool.index(key)
        self.__kpool.pop(index)
        self.__vpool.pop(index)
        return value

    def __iter__(self):
        return self.__kpool.__iter__()
    
    def __str__(self):
        s = ''
        for x in self.__kpool:
            tmp = x.__repr__() + ': ' + super(OrderedDict, self).__getitem__(x).__repr__() + ', '
            s += tmp
        return '{' + s[:-2] + '}'

    __repr__ = __str__ 

class DeepDict(Dict):

    """a dictionary with any deep assignment"""

    def __getitem__(self, key):
        if key not in self:
            tmp = self.__class__()
            super(DeepDict, self).__setitem__(key, tmp)
            return tmp
        return super(DeepDict, self).__getitem__(key)
