list1 = [{'name': 'Nick', 'age': 29},
         {'name': 'Linda', 'age': 28},
         {'name': 'Mike', 'age': 31}]

list1.sort(key=lambda x: x['age'])
print(list1)


dict1 = {'Mike': 45, 'Linda': 29, 'Nick': 34}
dict2 = sorted(dict1.items(), key=lambda x: x[1])
print(dict2)
