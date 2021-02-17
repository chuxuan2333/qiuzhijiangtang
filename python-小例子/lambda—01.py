def num():
    return [lambda x: i*x for i in range(5)]


print(num())
print([f(2) for f in num()])
print(num()[0](2))
print(num()[1](2))
print(num()[2](2))
print(num()[3](2))
print(num()[4](2))
