from distutils.core import setup
# name:模块名称
# version:版本号
# description:描述
# author:作者
# py_modules:要发布的内容
setup(name="calculator", version="1.0", description="加减乘除算法",
      author="chuxuan", py_modules=['calculator'], requires=['pymysql'])