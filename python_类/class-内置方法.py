class Person(object):
    def __init__(self, name, age, pro):
        """
        初始化实例对象
        :param name:
        :param age:
        :param pro: 专业
        """
        print("执行__init__函数...")
        self.name = name
        self.age = age
        self.pro = pro
        pass

    def __new__(cls, *args, **kwargs):
        """
        创建实例对象的方法
        :param args:
        :param kwargs:
        """
        print("执行__new__函数...")
        print("cls:{}".format(cls))
        return object.__new__(cls)  # 真正创建对象实例

        pass

    def __str__(self):
        print("执行__str__函数...")
        return "name:{},age:{},pro:{}".format(self.name, self.age, self.pro)
        pass

    # 将实例对象以函数的形式调用
    def __call__(self, *args, **kwargs):
        print("执行__call__函数...")
        return "name:{},age:{},pro:{}".format(self.name, self.age, self.pro)

    def __del__(self):
        print("执行__del__函数...")
        print("系统回收对象{}".format(self.name))
    pass


ming = Person("小明", "22", "计算机")
print(ming)
print("*"*40)

print("__class__功能和type()函数一样，都是查看对象所在的类...")
print("ming:", type(ming), "Person:", type(Person))
print(ming.__class__, Person.__class__, ming.__class__.__class__)
print("*"*40)

hong = Person("小红", "20", "数学")
print(hong)
print(hong())
