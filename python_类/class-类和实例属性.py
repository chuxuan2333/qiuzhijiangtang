class Student(object):
    name = '李明'  # 类属性

    def __init__(self, age):
        self.age = age  # 实例属性
        pass


Lm = Student(15)
print('类对象:', Lm.name)
print('类对象:', Lm.age)
print('类:', Student.name)
# print('类:', Student.age)  # 类不能访问实例属性
print('*'*30)
Lm.name = '张三'             # 对象Lm创建了一个name属性
print('类对象:', Lm.name)
print('类:', Student.name)
print('*'*30)
Student.name = '李四'
print('类对象:', Lm.name)
print('类:', Student.name)
