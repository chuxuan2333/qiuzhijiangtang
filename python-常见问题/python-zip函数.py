def BookInfo():

    # bookid = input("输入编号：").split(' ')
    # bookname = input("输入书名：").split(' ')
    # bookpos = input("输入货架号：").split(' ')

    bookid = [1, 2, 3]
    bookname = ['python', 'java', 'C++']
    bookpos = ['h2', 'b3', 'd5']

    # zip函数使用
    bookinfo = zip(bookid, bookname, bookpos)

    books = []
    for item in bookinfo:
        book = {"编号": item[0], "书名": item[1], "货架号": item[2]}
        books.append(book)

    for item in books:
        print(item)


BookInfo()

# zip函数效果展示
tzip = zip([1, 2, 3], ['a', 'b', 'c'], ["@", "#", "$"])
print(list(tzip))
