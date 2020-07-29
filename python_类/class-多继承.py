class Anmial:
    @staticmethod
    def run(name):
        print("{}在跑".format(name))

    def running(self):
        print("{}在跑".format(self.name))


class Bird:
    def fly(self):
        print("{}会飞".format(self.name))


class Dog(Anmial):
    name = '狗'

    def like(self):
        print("{}喜欢吃骨头".format(self.name))


class Cat(Anmial):
    name = '猫'

    def like(self):
        print("{}喜欢吃鱼".format(self.name))


class Parrot(Anmial, Bird):
    name = '鹦鹉'
    pass


dog = Dog()
dog.run(dog.name)
dog.running()
dog.like()
print('*'*30)
cat = Cat()
cat.run(cat.name)
cat.running()
cat.like()
print('*'*30)
parrot = Parrot()
parrot.running()
parrot.fly()
