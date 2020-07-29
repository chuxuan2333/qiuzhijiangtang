# https://mp.weixin.qq.com/s?__biz=MzAwOTQ4MzY1Nw==&mid=2247483690&idx=1&sn=322df4da624d7caf3eb22a5468280d7a&chksm=9b5fa5ccac282cda0eb15b8585aa34ff2f31e2f8537e14ca0a1c4894775799e82a7f614c88ca&scene=21#wechat_redirect

# Python中通过引用计数法来进行内存的管理的

import sys

s = "Hello"
print(sys.getrefcount(s))
a = s
print(sys.getrefcount(s))
print(id(s) == id(a))
print(s is a)

# Python中的变量在内存中的分配主要有两种，一种是简单拷贝，比如list，
# 改变一个就会引起另一个的改变，这是因为它们的引用相同，指向了同一个对象：
L = [3, 4, 5]
LL = L
L.append(6)
print(L, LL)
print(id(L) == id(LL))  # True


# 另外一种是深度拷贝，如数值、字符串、元组（tuple不允许被更改)等，也就是说
# 当将变量a赋值给变量b时，虽然a和b的内存空间仍然相同，但当a的值发生变化时，
# 会重新给a分配空间，a和b的地址变得不再相同。
a = "abc"
b = a
a = "xyz"
print(a, b)
print(id(a) == id(b))   # False


