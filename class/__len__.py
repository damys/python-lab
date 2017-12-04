# __len__ 可以用len()函数返回Students实例的“长度”

class Students(object):

    def __init__(self, *args):
        self.names = args
        
    def __len__(self):
        return len(self.names)

s = Students('tom', 'jack')
print( len(s) )


# 如果一个类表现得像一个list，要获取有多少个元素，就得用 len() 函数
# 注：要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，它返回元素的个数
