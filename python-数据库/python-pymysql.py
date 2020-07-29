import pymysql

connect = pymysql.connect(host='localhost',
                          port=3306,
                          user='chuxuan',
                          password='123456',
                          database='test',
                          charset='utf8')
