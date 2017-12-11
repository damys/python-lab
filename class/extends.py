"""
子类拥有父类所有的方法和属性， 当父类的方法不能满足子类需求时，可以进行重写
扩展的方式
在子类中重父类的方法
在需要的位置使用super().父类的方法 来调用父类方法
supper 是一个特殊的类， 常用于调用父类中封装的方法

子类对象 不能在自己的方法内部， 直接访问父类私有属性和私有方法
子类对象 可能通过 父类的公有方法间接访问到私有属性 或私有方法
"""


class A:
     
    def a(self):
        print('a...')
 
    def __test(self):
        print('Private...test')
 
    def call_test(self):
        self.__test()
 
 
class B(A):
 
    def b(self):
        print("b...")
 
    def show(self):
        print("show b...")
 
 
class C(B):
 
    def c(self):
        print("c...")
 
        super().show()  # 调用父类方法方式1: super().方法名()
        C.show(self)    # 调用父类方法方式2: 类名:方法(self) --- 不推荐(Python 2.x)
 
    # 重写
    def show(self):
        print("show c...")
 
        # super().show() # 不会出现递归调用
        # C.show(self)   # 在相同的方法里递归调用
 
 
    def other(self):
        print("other...")
 
 
c = C()
c.a()
c.b()
c.c()
 
c.show()
 
c.call_test()    # 调用私有方法, 通过父类共用方法
