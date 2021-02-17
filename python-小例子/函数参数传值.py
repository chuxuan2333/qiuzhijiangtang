def change_num(a):
    a += 1


def change_list(a):
    a.append(5)


n = 1
list1 = [1, 2, 3]
change_num(n)
change_list(list1)
print(n)
print(list1)

# 函数的参数是值传递，