class User:
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, uid):
        self.__uid = uid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return "uid:{},name:{}".format(self.__uid, self.__name)

    def __call__(self, *args, **kwargs):
        return "uid:{},name:{}".format(self.__uid, self.__name)


user = User(123400, "张三")
print(user.uid, user.name)
user.uid = 123401
user.name = "王五"
print(user)        # 对应__str__()方法
print(user())      # 对应__call__()方法，将实例对象以函数的形式调用