def MetaClassGetattribute(self, item):

    """reconstruct __getattribute__ in metaclass"""

    def class_lookup(cls, item):
        v = cls.__dict__.get(item)
        if v is not None:
            return v, cls
        for x in cls.__bases__:
            v, c = class_lookup(x, item)
            if v is not None:
                return v, c
        return None, None

    v, cls = class_lookup(type(self), item)
    if (v is not None) and hasattr(v, '__get__') and hasattr(v, '__set__'):
        return v.__get__(self, cls)
    w = self.__dict__.get(item)
    if w is not None:
        if hasattr(w, '__get__'):
            return w.__get__(None, self)
        else:
            return w
    if v is not None:
        if hasattr(v, '__get__'):
            return v.__get__(self, cls)
        else:
            return v
    raise AttributeError(type(self), item)
    
def ClassGetattribute(self, item):

    """reconstruct __getattribute__ in class"""
    
    def class_lookup(cls, item):
        v = cls.__dict__.get(item)
        if v is not None:
            return v, cls
        for x in cls.__bases__:
            v, c = class_lookup(x, item)
            if v is not None:
                return v, c
        return None, None

    v, cls = class_lookup(type(self), item)
    if (v is not None) and hasattr(v, '__get__') and hasattr(v, '__set__'):
        return v.__get__(self, cls)
    w = self.__dict__.get(item)
    if w is not None:
        return w
    if v is not None:
        if hasattr(v, '__get__'):
            return v.__get__(self, cls)
        else:
            return v
    raise AttributeError(type(self), item)
