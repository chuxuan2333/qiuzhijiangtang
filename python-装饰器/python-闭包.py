# 闭包的作用：保存外部函数的变量, 装饰器
# 闭包形成条件：
# 1. 函数嵌套
# 2. 内部函数使用了外部函数的变量或参数
# 3. 外部函数返回内部函数
#    则将内部函数称之为闭包


def func_out(arg):
    def func_in(x):
        return arg+x
    return func_in


func = func_out(10)
print(func(1))
print(func(10))


# 闭包的应用：接收不同参数返回不同的处理结果
def config_name(name):
    def talk(msg):
        print(name + ':' + msg)
    return talk


tom = config_name("Tom")
jim = config_name("Jim")
tom("My name is Tom")
jim("My name is Jim")
tom("L come from China")
jim("I come from America")