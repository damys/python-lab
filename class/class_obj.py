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
