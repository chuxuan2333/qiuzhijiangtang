class ClassDecorator:
    def __init__(self, func):
        self.func = func
        self.name = '类装饰器'
        pass

    # 实现__call__()方法可以让类对象以函数的形式调用
    def __call__(self, *args, **kwargs):
        print("对已有函数进行封装")
        res = self.func(args[0], args[1])
        return res


@ClassDecorator     # add1 = ClassDecorator(add1)
def add1(x, y):
    print("执行原函数")
    return x + y


# add1 是ClassDecorator类实例对象
print(add1.name)
print(add1(2, 3))