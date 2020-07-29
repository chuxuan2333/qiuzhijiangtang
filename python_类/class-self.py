class Person(object):
    def eat(self):
        print("self:%s" % self)
        print("self:%s" % id(self))

    def run(self):
        print("this:", self)
        print("this:{}".format(id(self)))
    pass


zh = Person()
zh.eat()
print("zh:", zh)
print("zh:", id(zh))
zh.run()
