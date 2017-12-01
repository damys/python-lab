# 生命周期结束， 可以删除一个对象

class Cat:
    """这是一个猫类"""
 
    def __init__(self, name):
        print("初始化开始...")
        self.name = name
 
    def eat(self):
        print("%s eat fish" % self.name)
 
    def drink(self):
        print("%s drink water" % self.name)
 
    def __del__(self):
        print("%s goodby. 对象在销毁前调用.--生命周期结束" % self.name)
 
tom = Cat("Tom")
tom.drink()
print(tom.name)
 
# del tom
 
print('-' * 30)
lazy_cat = Cat("懒猫")
lazy_cat.eat()
 
"""
输出：
初始化开始...
Tom drink water
Tom
------------------------------
初始化开始...
懒猫 eat fish
Tom goodby. 对象在销毁前调用
生命周期结束
懒猫 goodby. 对象在销毁前调用
生命周期结束
 
 
-------------------------------------------
-  将上面注释放开，执行： del tom, 输出：
-------------------------------------------
初始化开始...
Tom drink water
Tom
Tom goodby. 对象在销毁前调用.--生命周期结束
------------------------------
初始化开始...
懒猫 eat fish
懒猫 goodby. 对象在销毁前调用.--生命周期结束
"""
