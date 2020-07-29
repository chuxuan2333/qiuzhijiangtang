import types


class User:
    def __init__(self, uid):
        self.__uid = uid


# 定义实例方法
def print1(self):
    print("name:{}".format(self.name))


# 定义类方法
@classmethod
def print2(cls):
    print("User School:{}".format(cls.school))


# 定义静态方法
@staticmethod
def print3():
    print("静态方法")


user1 = User(1001)
user2 = User(1002)

user1.name = "张三"         # 动态绑定实例属性
user2.name = "李四"
User.school = "上海大学"     # 动态绑定类属性

# 动态绑定实例方法
user1.print_user1 = types.MethodType(print1, user1)

# 动态绑定类方法
User.print_U = print2
# 动态绑定静态方法
User.print_u = print3


print(user1.name, user1.school)
print(user2.name, user2.school)
user1.print_user1()         # 调用动态实例方法
user1.print_U()             # user1调用动态类方法
user2.print_U()             # user2调用动态类方法
user1.print_u()             # 调用静态方法

