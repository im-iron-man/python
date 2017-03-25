def Id(obj):
    return id(obj)
    
def Type(obj):
    return type(obj)

def Name(obj):
    if '__name__' in dir(obj):
        return obj.__name__
    
def Doc(obj):
    return obj.__doc__
    
def Dict(obj):
    if '__dict__' in dir(obj):
        return obj.__dict__

def Class(obj):
    return obj.__class__

def Bases(obj):
    if '__bases__' in dir(obj):
        return obj.__bases__
    
def Module(obj):
    if '__module__' in dir(obj):
        return obj.__module__
    else:
        return globals()['__name__']

def isMetaclass(obj):
    if '__bases__' in dir(obj) and type in obj.__bases__:
        return True
    else:
        return False

def isClass(obj):
    if '__bases__' in dir(obj) and type not in obj.__bases__:
        return True
    else:
        return False

def isInstance(obj):
    if '__bases__' not in dir(obj):
        return True
    else:
        return False
