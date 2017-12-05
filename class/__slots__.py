# 一个类允许的属性列表
## 目的是限制当前类所能拥有的属性，如果不需要添加任意动态的属性，使用__slots__也能节省内存

class Student(object):
     
    __slots__ = ('name', 'gender')
 
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
 
s = Student('jack', 'male')
print(s.name)
print(s.gender)
 
s.age = 25
print(s.age)
