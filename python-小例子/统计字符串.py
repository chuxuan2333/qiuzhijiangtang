from collections import Counter


def count_str(s):
    dict1 = {}
    for i in s:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1


test_str = r'1zcrs42438%$723、。，。、|、、\\\////*&^^$$#!'
print(count_str(test_str))

# 使用collections模块的Counter方法
print(Counter(test_str))
