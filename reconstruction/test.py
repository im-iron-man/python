from reconstruction.Integer import Integer
from reconstruction.Float import Float
from reconstruction.String import String
from reconstruction.List import List
from reconstruction.Tuple import NamedTuple
from reconstruction.Dictionary import Dict
from reconstruction.Set import Set
from reconstruction.MagicMethod import ClassGetattribute
from reconstruction.Descriptor import ClassMethod
from reconstruction.Call import IntAdd

# test Integer
i = Integer(1)
print i

# test Float
f = Float(1.0)
print f

# test String
s = String('1')
print s

# test List
l = List([1, 2])
print l

# test Tuple
point = NamedTuple('point', ['x', 'y'])
p = point(1, 2)
print p.x
print p.y

# test Dictionary
d = Dict({1: 'a'})
d.update({2: 'b'})
print d

# test Set
s = Set([1, 2])
print s

# test Magic Method
class A(object):

    def __init__(self, a):
        self.a = a

A.__getattribute__ = ClassGetattribute
print A('xyz').a

# test Descriptor
class Person(object):

    @ClassMethod
    def f(cls):
        return cls

print Person.f()

# test Call
print IntAdd(1)(2)
print IntAdd(1)(2)(3)
