"""
在python中，一个.py文件就是一个模块

import首次导入模块的时候，会发生3步操作：
1. 打开模块文件
2. 执行模块对应的文件，将执行过程中产生的名称加入到模块的命名空间中
3. 在程序中会有一个模块的名称指向模块命名空间
from XXX import XXX
import XXX as XXX
"""

import time
# 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
print(time.time())
# 返回一个时间元祖
print(time.ctime())
# 格式化时间戳为本地时间
print(time.localtime())
# 返回格式化时间字符串
print(time.strftime("%Y %m %d %H:%M:%S", time.localtime()))


# OS 模块
import os
# 获取当前目录
print(os.getcwd())
# 路径拼接
print(os.path.join(os.getcwd(), "newdir"))
