
# exp2 读文件
with open("./files/test1.txt", 'r') as f:
    # read():一次性读取文件全部内容
    content1 = f.read(8)
    print("content1:" + content1)
    content2 = f.read()
    print("content2:" + content2)
print('*'*40)

with open('./files/test1.txt') as f:
    # 读取所有行，以列表形式保存
    cont = f.readlines()
    print("cont:", cont)
    for c in cont:
        print('c:' + c)
print('*'*40)

with open('./files/test3.txt', 'r') as f:
    # 读取一行
    cont = f.readline()
    print('读取一行：' + cont)
print('*'*40)

with open('./files/test2.txt', 'rb') as f:
    # 以二进制形式读取文件
    cont = f.read()
    print('二进制读取：', end='')
    print(cont)
    print("cont:" + cont.decode('utf-8'))