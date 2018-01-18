"""
类对象创建的个数


访问类属性有两种方式：类名.类属性， 对象.类的属性（不推荐）
注意：如果使用对象.类属性 = 值赋值语句，只会给对象添加一个属性，而不会影响到类属性的值
"""

class Tool(object):
     
    # 记录所有工具对象的数据
    count = 0
 
    def __init__(self, name):
        self.name = name
 
        Tool.count += 1
 
tool1 = Tool('A1')
tool2 = Tool('A2')
tool3 = Tool('A3')


print('工具对象总数 %d' % Tool.count)  # 3
print('工具对象总数 %d' % tool2.count) # 3
print('工具对象总数 %d' % tool3.count) # 3
 
# 属性的获取机制：存在一个向上查找机制
tool3.count = 99
print('工具对象总数 %d' % Tool.count)  # 3
print('工具对象总数 %d' % tool3.count) # 99


'''
实例方法 -- 方法内部需要访问实例的属性
类方法 ---- 方法内部只需要访问类属性
静态方法 -- 方法内部不需要访问实例属性和类属性
'''
