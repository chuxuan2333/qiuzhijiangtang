import random


def bin_search(arg_list, value):
    """
    折半查找, 非递归
    :param arg_list:
    :param value:
    :return: arg_list.index(value) or False
    """
    low = 0
    high = len(arg_list) - 1
    while high >= low:
        mid = (low+high)//2
        mid_value = arg_list[mid]
        if arg_list[mid] == value:
            return mid
        elif arg_list[mid] > value:
            high = mid-1
        else:
            low = mid+1
    else:
        return False


def bin1_search(arg_list, value):
    """
    折半查找, 递归
    :param arg_list:
    :param value:
    :return: arg_list.index(value) or False
    """
    length = len(arg_list)
    while length > 0:
        mid = length//2
        mid_value = arg_list[mid]
        if arg_list[mid] == value:
            return True
        elif arg_list[mid] > value:
            return bin1_search(arg_list[:mid-1], value)
        else:
            return bin1_search(arg_list[mid+1:], value)
    else:
        return False


test_list = [random.randint(0, 100) for i in range(100)]
test_list.sort()
print(test_list)
print(bin1_search(test_list, 35))

