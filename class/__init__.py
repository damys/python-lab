class Cat:
    """这是一个猫类"""
 
    def __init__(self):
        print("初始化方法")
 
    def eat(self):
        print("Cats eat fish")
 
    def drink(self):
        print("Cats drink water")
 
# 第一个对象调用前都会执行 __init__
tom = Cat()
tom.drink()             # Cats drink water
 
print(tom)              # 内存地址：<__main__.Cat object at 0x0000000001EFA278>
print("%d" % id(tom))   # 以10 进制 32481912
print("%x" % id(tom))   # 以16 进制 1efa278
 
lazy_cat = Cat()
lazy_cat.eat()          # Cats eat fish
print(lazy_cat)         # 内存地址：<__main__.Cat object at 0x0000000001EFA320>
 
# 不推荐：类的外部添加属性， 如未找到会报错
lazy_cat.name = 'lazy'
