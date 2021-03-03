def reverse_int(x):
    if not isinstance(x, int):
        return False

    if x < 0:
        return int('-' + str(x)[1:][::-1])
    else:
        return int(str(x)[::-1])


print(reverse_int(-123001))
