# 伪私有属性和私有方法
"""
在Python 中，并没有真正的私有
在级属性，方法命名时，实际是对名称做了一些特殊处理，使得外界无法访问到
处理方式：在名称前面加上: 定义__类名， 调用：_类名__名称
"""

class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有
 
    def __secret(self):
        return  self.__age
 
 
if __name__ == '__main__':
    rose = Women('rose')
 
    # 伪属性，方法
    print(rose._Women__age)       # 18
    print(rose._Women__secret())  # 18
