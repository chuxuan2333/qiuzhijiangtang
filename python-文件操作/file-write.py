
# exp1 文件写入
with open("./files/test1.txt", 'w+', encoding='gbk') as file:
    file.write("以读写覆盖的形式打开一个文件。\r")
    file.write("在苍茫的大海上，\n狂风卷积着乌云。")
    pass

with open('./files/test2.txt', 'wb+') as file:
    # str ——> bytes
    file.write("以二进制的形式打开一个文件并写入数据。".encode('utf-8'))
    pass

with open("./files/test3.txt", 'a+') as file:
    file.write("以追加的形式打开一个文件。\n")
    file.write("窗前明月光，疑是地上霜。")
    pass