def validateLogin(func):
    print("加载装饰器")

    # 内部函数与被装饰函数参数一致
    def inner(msg):
        print("函数执行前添加功能")
        res = func(msg)   # 执行原函数,并接收返回值
        print("函数执行后添加功能")
        return res
    return inner


@validateLogin
def comment(msg):
    print(msg)
    return 1


res1 = comment('res1发表评论')
res2 = comment('res2发表评论')
print(res1)
print(res2)

print('*'*40)


# 带参数的装饰器：其实就是定义了一个带参数的函数，返回了一个装饰器
def return_decorator(flag, msg):
    print(msg)

    def decorator(func):
        print("加载装饰器...")

        def inner(x, y):
            if flag == "+":
                print('加法运算')
            elif flag == '-':
                print('减法运算')
            res = func(x, y)
            print(res)
        return inner
    return decorator


@return_decorator('+', '带参数的装饰器')
def add1(x, y):
    return x+y


@return_decorator('-', '带参数的装饰器')
def sub1(x, y):
    return x-y


add1(3, 4)
sub1(3, 4)

