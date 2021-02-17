import json
# dumps()：将字典转换为JSON格式的字符串
# loads()：将JSON格式的字符串转化为字典
# dump()：将字典转换为JSON格式的字符串，并将转化后的结果写入文件
# load()：从文件读取JSON格式的字符串，并将其转化为字典

# 字典转json
dict1 = {'name': 'Linda', 'age': 18, 'sex': 'female'}
json1 = json.dumps(dict1)
print('json1:', json1)
print(type(json1))

# json字符串转字典
json2 = '{"name": "Jack", "age": 24, "sex": "male"}'
dict2 = json.loads(json2)
print('dict2:', dict2)
print(type(dict2))

# 读取json文件并转化成字典
with open('json_file/jack.json', 'r') as f:
    dict3 = json.load(f)
    print('dict3:', dict3)

# 将字典转换为JSON字符串，并写入文件
with open('json_file/linda.json', 'w') as f:
    json.dump(dict1, f)
