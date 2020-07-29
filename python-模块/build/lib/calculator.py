
# 自定义模块
# __all__变量中的元素会被from XXX import * 语法导入
# add , subtract , multiply and divide
__all__ = ['add1', 'sub1', 'mul1', 'div1']


def add1(x, y):
    return x+y


def sub1(x, y):
    return x-y


def mul1(x, y):
    return x*y


def div1(x, y):
    return x/y