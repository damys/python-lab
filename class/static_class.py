"""
不需要访问实例属性，调用实例方法， 类属性， 类方法， 使用@staticmethod修饰
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
 
 
    @staticmethod
    def show_help():
        print("help message ....")
 
 
# 调用静态方法
Tool.show_help()
