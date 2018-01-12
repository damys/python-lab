"""
类属性：就是针对类对象定义的属性：特征
类方法：就是针对类对象定义的方法。 第一个参数为cls, 类的引用，与self类似
在方法内部：可以通过cls.访问类的属性，其它类的方法， 使用@classmethod修饰
"""

class Tool(object):
     
    # 记录所有工具对象的数据
    count = 0
    
    def __init__(self, name):
        self.name = name
 
        Tool.count += 1
 
    @classmethod
    def show_tool_count(cls):
        print('工具对象总数 %d' % cls.count)
 
 
 
tool1 = Tool('A1')
tool2 = Tool('A2')
tool3 = Tool('A3')
