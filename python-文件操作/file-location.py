"""
# 文件定位操作，返回当前文件指针读取的位置
# tell()返回文件指针当前的(字节)位置
truncate() 从文件当前位置起截断；截断size字节的字符
指定长度的话，就从文件的开头开始截断指定长度，其余内容删除；
不指定长度的话，就从文件开头开始截断到当前位置，其余内容删除。
"""
"""
seek(offset, from): 参数offset，正数向前偏移n字节，负数向后偏移
n字节，参数from，0表示文件开头，1表示当前位置，2表示文件末尾。
"""

with open('./files/test2.txt', 'rb') as f:
    print(f.read(5))
    print(f.tell())
    print(f.read(3))
    print(f.tell())

with open('./files/test1.txt', 'r') as f:
    print(f.read(5))
    print(f.tell())
    print(f.read(3))
    print(f.tell())

with open('./files/test1副本.txt', 'r+') as f:
    # 截取6个字节的数据
    f.truncate(6)
    print(f.read())
