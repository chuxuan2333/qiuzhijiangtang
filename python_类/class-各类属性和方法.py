class Animal(object):  # 类对象

    age = 3  # 公有类属性
    __like = None  # 私有类属性

    def __init__(self):  # 构造方法
        self.name = '狗'  # 公有实例属性
        self.__sex = 'man'  # 私有实例属性

    def smile(self):  # 公有方法  self指向实例对象
        pass

    def __jump(self):  # 私有方法
        pass

    @classmethod
    def run(cls):  # 类方法  cls 指向类对象
        pass

    @staticmethod
    def msg():  # 静态方法，可以没有参数
        pass


anmial = Animal()
print(anmial.name, anmial.age)
