# __len__ 可以用len()函数返回Students实例的“长度”

class Students(object):

    def __init__(self, *args):
        self.names = args
        
    def __len__(self):
        return len(self.names)

s = Students('tom', 'jack')
print( len(s) )
