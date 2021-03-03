import random
import string


def generate_pwd(n):
    """
    生成n位数的随机码
    :param n:
    :return:
    """
    chars = string.digits + string.ascii_letters + string.punctuation
    # print(chars)
    pwd = [random.choice(chars) for i in range(n)]
    return ''.join(pwd)


print(generate_pwd(8))