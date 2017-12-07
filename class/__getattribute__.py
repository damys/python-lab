class Person(object):
     
    def __init__(self, name, age):
        self.name = name
        self.age  = age
 
    # 在访问一个存在的属性时,新增提示功能
    def __getattribute__(self, name):
        print("你正在访问一个存在属性")
 
        # return getattr(self, name)       # 递归错误，默认1000次
        # return self.__dict__[name]       # 递归错误，默认1000次
        return super(Person, self).__getattribute__(name)
 
    # 找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常
    def __getattr__(self, name, value):
        # setattr(self, name, value)
        self.__dict__[name] = value
 
 
if __name__ == '__main__':
    p = Person('jaon', 25)
    print(p.name)

"""
你正在访问一个存在属性
jaon
"""
