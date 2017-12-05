"""
In [1]: f = abs
 
In [2]: f.__name__
Out[2]: 'abs'
 
In [3]: f(-23)
Out[3]: 23
 
由于 f 可以被调用，所以，f 被称为可调用对象
所有的函数都是可调用对象
 
 
 
一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
"""
class Person(object):
 
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
 
    def __call__(self, friend):
        print('my name is %s' % self.name)
        print('my friend is %s' % friend)
 
p = Person('jack', 'male')
p("TOM")
 
my name is jack
my friend is TOM

"""
单看 p('TOM') 你无法确定 p 是一个函数还是一个类实例，所以，在Python中，函数也是对象，对象和函数的区别并不显著
"""
