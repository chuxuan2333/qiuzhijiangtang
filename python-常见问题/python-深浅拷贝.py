# 在Python中，通过一个对象向另外一个对象赋值，
# 实际仅仅是赋值了对象的引用，而非创建一个对象并赋值。

Anndy = ['Anndy', ['age', 24]]
Tim = Anndy             # 引用复制
Tom = Anndy[:]          # 浅拷贝
Cindy = list(Anndy)     # 浅拷贝
print(id(Anndy))
print(id(Tim))
print(id(Tom))
print(id(Cindy))
print('*'*40)

Tom[0] = 'Tom'
Cindy[0] = 'Cindy'
print(Anndy, Tom, Cindy)   # 修改姓名没有问题

Tom[1][1] = 12
print(Anndy, Tom, Cindy)   # 所有人的年龄都被修改了

# 打印列表中各个元素的ID, 第二个元素的ID是相同的
# 原因就是构造方法或切片 [:] 是浅拷贝, 只拷贝了最外层容器
print([id(x) for x in Anndy])
print([id(x) for x in Tom])
print([id(x) for x in Cindy])
print('*'*40)

# 深拷贝，不仅拷贝最外层容器，还会拷贝容器中的元素。
# 利用copy中的deepcopy方法来实现。
import copy
x = ['abc', ['name', 23]]
y = copy.deepcopy(x)
print(id(x), id(x[0]), id(x[1]), id(x[1][0]), id(x[1][1]))
print(id(y), id(y[0]), id(y[1]), id(y[1][0]), id(y[1][1]))
