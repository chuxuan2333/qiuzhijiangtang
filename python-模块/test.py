"""
导入自定义模块
"""
import calculator as c
from calculator import *

print(c.__all__)
x, y = 30, 12
print(add1(x, y))
print(sub1(x, y))
print(mul1(x, y))
print(div1(x, y))
