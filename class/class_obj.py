class Tool(object):
     
    # 记录所有工具对象的数据
    count = 0
 
    def __init__(self, name):
        self.name = name
 
        Tool.count += 1
 
tool1 = Tool('A1')
tool2 = Tool('A2')
tool3 = Tool('A3')
