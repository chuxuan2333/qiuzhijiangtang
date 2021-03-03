import random


def permutation(arg_list, n=3):
    """
    列表arg_list中选n个排列
    :param arg_list:
    :param n:
    :return:
    """
    for i in arg_list:
        for j in arg_list:
            for k in arg_list:
                if i != j and i != k and j != k:
                    print(i, j, k, end='  ')
        print()
    pass


def combination(arg_list, n=3):
    """
    列表arg_list中选n个组合
    :param arg_list:
    :param n:
    :return:
    """
    for i in arg_list:
        for j in arg_list:
            for k in arg_list:
                if i < j < k:
                    print(i, j, k, end='  ')
        print()
    pass


test_list = list(range(1, 6))
print(test_list)
print('全排列：')
permutation(test_list)
print('全组合：')
combination(test_list)



