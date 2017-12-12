"""
新式类与旧式（经典）类

object 是python 为所有对象提供的基类， 提供有一些内置的属性和方法，可以使用dir函数查看
python 2.x 中定义类时，如果没有指定， 则不会以object作为基类
"""

class className(object):
    pass
    
    
    
print(dir(A()))
['__doc__', '__module__']
 
 
 
class B(object):
    pass
 
print(dir(B()))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
 
