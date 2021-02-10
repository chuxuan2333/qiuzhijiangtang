def change(s):
    dict1 = {
        'A1': 'A1', 'A2': 'A2', 'A3': 'A3', 'A4': 'A4', 'A5': 'A5',
        'A6': 'B1', 'A7': 'B2', 'B1': 'B3', 'B2': 'B4', 'B3': 'B5',
        'B4': 'C1', 'B5': 'C2', 'B6': 'C3', 'B7': 'C4', 'C1': 'C5'
    }
    if s in dict1.keys():
        return dict1[s]
    else:
        pass


def make_yuepu(*args):
    return list(map(change, *args))
    pass


tiankongzhicheng = ['A6', 'A7', 'B1', 'A7', 'B1', 'B3', 'A7', 'A3', 'A6', 'A5', 'A6', 'B1', 'A5',
                    'A3', 'A3', 'A4', 'A3', 'A4', 'B1', 'A3', 'B1', 'B1', 'A7', 'A4', 'A4', 'A7', 'A7',
                    'A6', 'A7', 'B1', 'A7', 'B1', 'B3', 'A7', 'A3', 'A6', 'A5', 'A6', 'B1', 'A5',
                    'A2', 'A3', 'A4', 'B1', 'A7', 'B1', 'B2', 'B2', 'B3', 'B1', 'B1', 'A7', 'A6', 'A6', 'A7', 'A5', 'A6',
                    'B1', 'B2', 'B3', 'B2', 'B3', 'B5', 'B2', 'B1', 'B1', 'A7', 'B1', 'B3', 'B3',
                    'A6', 'A7', 'B1', 'A7', 'B1', 'B2', 'B1', 'A5', 'A5', 'B4', 'B3', 'B2', 'B1', 'B3',
                    'B3', 'B6', 'B6', 'B5', 'B5', 'B3', 'B2', 'B1', 'B2', 'B1', 'B2', 'B5', 'B3',
                    'B3', 'B6', 'B6', 'B5', 'B5', 'B3', 'B2', 'B1', 'B2', 'B1', 'B2', 'A7', 'A6'
                    ]

output = ' '.join(tiankongzhicheng)
# output = ' '.join(make_yuepu(tiankongzhicheng))

print("天空之城:", output)
