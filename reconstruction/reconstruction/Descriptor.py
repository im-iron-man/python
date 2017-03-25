class ClassMethod(object):

    "reconstruct __builtins__.classmethod"
    
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, typ=None):
        return self.f.__get__(typ, type)

class StaticMethod(object):

    "reconstruct __builtins__.staticmethod"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, typ=None):
        return self.f

class Property(object):

    "reconstruct __builtins__.property"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if not doc and not fget:
            doc = fget.__doc__
        self.__doc__ = doc
        
    def __get__(self, obj, typ=None):
        if not obj:
            return self
        if not self.fget:
            raise AttributeError('unreadable attribute')
        return self.fget(obj)
        
    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError('can\'t set attribute')
        self.fset(obj, value)
        
    def __delete__(self, obj):
        if not self.fdel:
            raise AttributeError('can\'t delete attribute')
        self.fdel(obj)
        
    def getter(self, fget):
        return self.__class__(fget, self.fset, self.fdel, self.__doc__)
    
    def setter(self, fset):
        return self.__class__(self.fget, fset, self.fdel, self.__doc__)
        
    def deleter(self, fdel):
        return self.__class__(self.fget, self.fset, fdel, self.__doc__)
