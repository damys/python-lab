"""
多态不同的子类对象调用相同的父类方法，产生不同的结果， 增加代码灵活度，不会影响到类的内部设计
类具有继承关系，并且子类类型可以向上转型看做父类类型，如果我们从 Person 派生出 Student和Teacher ，并都写了一个 whoAmI() 方法：
"""


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name
 
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name
 
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name
在一个函数中，如果我们接收一个变量 x，则无论该 x 是 Person、Student还是 Teacher，都可以正确打印出结果：
 
def who_am_i(x):
    print x.whoAmI()
 
p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
