"""
多继承
"""
class A:
     
    def a(self):
        print('a...')
 
class B:
 
    def b(self):
        print("b...")
 
 
class C(A, B):
 
    def c(self):
        print("c...")
 
c = C()
c.a()
c.b()
c.c()
 
 
# 从左到右顺序方法搜索, 搜索不到会报错
print(C.__mro__)
# (<class '__main__.C'$gt;, $lt;class '__main__.A'$gt;, $lt;class '__main__.B'$gt;, $lt;class 'object'$gt;)
