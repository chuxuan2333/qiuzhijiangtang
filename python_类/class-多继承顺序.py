class A:
    def run(self):
        print('A.running')
    pass


class B(A):
    def run(self):
        print('B.running')
    pass


class C(A):
    pass


class D(C, B):
    pass


class E(D, C):
    pass


d = D()
d.run()
print(D.__mro__)    # 打印类的继承顺序
print('*'*30)
e = E()
e.run()
print(E.__mro__)     # 打印类的继承顺序


