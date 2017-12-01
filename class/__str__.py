# 输出对象变量，默认会输出引用的对象。 注意：必须返回一个字符串

class Cat:
    """这是一个猫类"""
 
    def __init__(self, name):
        print("初始化开始...")
        self.name = name
 
    def __del__(self):
        print("%s goodby. 对象在销毁前调用.--生命周期结束" % self.name)
 
    def __str__(self):
        return 'I am is %s' % self.name
 
tom = Cat("Tom")
print(tom)
 
 
 """
输出：
初始化开始...
I am is Tom
Tom goodby. 对象在销毁前调用.--生命周期结束
"""
