import os
import time
"""
购物车程序功能：
1、启动程序后，输入用户名密码后，打印商品列表

2、允许用户根据商品编号购买商品

3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒

4、可随时退出，退出时，打印已购买商品和余额

5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

扩展功能：
1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买

2、允许查询之前的消费记录
"""


def select_user_info():
    # 读取用户信息文件,取出用户名、密码、锁定状态、余额组成一个用户信息字典user_info_dict
    with open(user_info_f_name, 'r', encoding='utf-8') as user_info_f:
        for line in user_info_f:  # 用户信息字符串
            user_info_list = line.strip().split(':')  # 将字符串转换为列表
            print(user_info_list) # 用户信息列表
            _username = user_info_list[0].strip()  # 用户名
            _password = user_info_list[1].strip()  # 密码
            _lock = int(user_info_list[2].strip())  # 锁定状态,int类型（0代表未锁定，1代表锁定）
            _money = user_info_list[3].strip()  # 余额
            user_info_dict[_username] = {'password': _password, 'lock': _lock, 'money': _money}  # 将列表转换为字典
            # print(user_info_dict)  # 用户信息字典


def update_user_info():
    # 修改用户信息后，更新user_info.txt文件内容
    with open(user_info_f_temp_name, "w", encoding="utf-8") as user_info_f_temp:
        for user in user_info_dict:  # 将字典转换为列表
            user_info_list_new = [user, str(user_info_dict[user]['password']), str(user_info_dict[user]['lock']),
                                  str(user_info_dict[user]['money'])]
            # print(user_info_list_new) # 更新后的用户信息列表
            user_info_str = ":".join(user_info_list_new)  # 将列表转换为字符串
            # print(user_info_str)  # 更新后的用户信息字符串
            user_info_f_temp.write(user_info_str + "\n")
    os.replace(user_info_f_temp_name, user_info_f_name)


def product_list():
    # 商品列表
    print("\n------------商品列表------------\n")  # 商品列表
    for index, product in enumerate(goods, 1):
        print("%s.%s %d" % (index, product['name'], product['price']))
    print("\n-------------------------------")


def select_shopping_history():
    # 读取消费记录
    with open(shopping_history_f_name, "r", encoding="utf-8") as shopping_history_f:
        print("\n---------您的消费记录----------\n")
        for line in shopping_history_f:
            shopping_history_list = line.strip().split('|')
            # print(shopping_history_list)
            _username = shopping_history_list[0].strip()
            _time = shopping_history_list[1].strip()
            _product = shopping_history_list[2].strip()
            if username in shopping_history_list:
                print("用户 {0} {1} 购买了 {2}".format(_username, _time, _product))
            else:
                pass
        print("\n-------------------------------")


def update_shopping_history():
    # 更新消费记录
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(shopping_history_f_name, "a", encoding="utf-8") as shopping_history_f:
        shopping_history_f.write("\n%s|%s|%s" % (username, now_time, goods[product_id - 1]['name']))


# 商品信息
goods = [
    {"name": "电脑", "price": 4000},
    {"name": "鼠标", "price": 200},
    {"name": "游艇", "price": 20000},
    {"name": "美女", "price": 1000},
    {"name": "T恤", "price": 50},
]

# 菜单栏
choice_info = """
【n】购买商品
【h】消费记录
【m】余额查询
【q】退出商城

-------------------------------
"""

shopping_carts = []  # 初始购物车为空
user_info_dict = {}  # 初始化用户信息字典为空
user_info_f_name = "./files/user_info.txt"  # 用户信息文件名
user_info_f_temp_name = "user_info.txt.temp"  # 用户信息临时文件名
shopping_history_f_name = "./files/shopping_history.txt"  # 消费记录
count = 0

# 主程序开始
select_user_info()  # 读取用户信息文件，组成user_info_dict字典
while count < 3:
    username = input('\n\033[34;1m请输入用户名:\033[0m').strip()
    if username not in user_info_dict:
        count += 1
        print("\n\033[31;1m用户名错误\033[0m")
    elif user_info_dict[username]['lock'] > 0:
        print("\n\033[31;1m%s 已被锁定,请联系管理员解锁后重新尝试\033[0m" % username)
        exit()
    else:
        while count < 3:
            password = input('\n\033[34;1m请输入密码:\033[0m').strip()
            if password == user_info_dict[username]['password']:
                print("\n--------欢迎 %s 登陆商城--------" % (username))
                if int(user_info_dict[username]['money']) == 0:  # money = 0表示是首次登陆的用户
                    while True:
                        money = input("\n\033[34;1m请输入您的工资：\033[0m")  # 工资只能是数字
                        if money.isdigit():
                            money = int(money)
                            user_info_dict[username]['money'] = money
                            update_user_info()  # 更新工资余额到文件
                            # print(money)
                            break
                        else:
                            print("\n\033[31;1m您的工资只能是数字！\033[0m")
                            continue
                else:
                    money = int(user_info_dict[username]['money'])
                    print("\n\033[31;1m您上次购物后的余额为：%s 元！\033[0m\n" % (money))
                while True:
                    product_list()  # 打印商品列表
                    print(choice_info)  # 选择信息
                    product_id = input("\033[34;1m请输入您要的操作：\033[0m").strip()
                    if product_id.isdigit():
                        product_id = int(product_id)
                        if len(goods) >= product_id >= 1:
                            if money >= goods[product_id - 1]['price']:
                                money -= goods[product_id - 1]['price']
                                shopping_carts.append(goods[product_id - 1]['name'])
                                print("\n\033[31;1m%s已购买成功！\033[0m\n" % (goods[product_id - 1]['name']))
                                update_shopping_history()  # 写入消费记录文件
                                user_info_dict[username]['money'] = money
                                update_user_info()  # 更新工资余额到文件
                            else:
                                print("\n\033[31;1m抱歉，%s购买失败！工资余额不足！\033[0m" % (goods[product_id - 1]['name']))
                        else:
                            print("\n\033[31;1m商品编号有误,请重新输入！\033[0m")
                    elif product_id == "q":
                        if len(shopping_carts) > 0:
                            print("\n\033[31;1m您本次购买的商品及商品数量如下：\033[0m\n")
                            shopping_carts_delRepeat = list(set(shopping_carts))  # 购物车列表去重
                            for index, product_carts in enumerate(shopping_carts_delRepeat, 1):
                                print("%s. %s * %d" % (
                                    index, product_carts, shopping_carts.count(product_carts)))  # 显示同一商品数量
                        else:
                            print("\n\033[31;1m您本次没有购买东西！\033[0m")
                        print("\n\033[31;1m您的工资余额为：%s 元！\033[0m\n" % (money))
                        exit()
                    elif product_id == "h":
                        select_shopping_history()
                        choice_continue = input("\n\033[34;1m回到菜单栏（直接按回车）：\033[0m").strip()
                        if choice_continue == 'y' or choice_continue == "Y" or choice_continue == "":
                            continue
                        else:
                            print("\n\033[31;1m操作失误，强制退出！\033[0m")
                            exit()
                    elif product_id == "m":
                        print("\n\033[31;1m您的工资余额为：%s 元！\033[0m\n" % (money))
                        choice_continue = input("\n\033[34;1m回到菜单栏（直接按回车）：\033[0m").strip()
                        if choice_continue == 'y' or choice_continue == "Y" or choice_continue == "":
                            continue
                        else:
                            print("\n\033[31;1m操作失误，强制退出！\033[0m")
                            exit()
                    else:
                        print("\n\033[31;1m输入有误，请重新输入！\033[0m")
            else:
                count += 1
                print('\n\033[31;1m密码错误\033[0m')
                continue
    if count >= 3:  # 尝试次数大于等于3时锁定用户
        if not username:
            print("\n\033[31;1m您输入的错误次数过多,且用户为空！\033[0m")
        elif username not in user_info_dict:
            print("\n\033[31;1m您输入的错误次数过多,且用户 %s 不存在！\033[0m" % username)
        else:
            user_info_dict[username]['lock'] += 1  # 修改用户字典（锁定状态设为1）
            # print(user_info_dict) # 更新后的用户信息字典
            update_user_info()  # 更新user_info.txt文件内容
            print("\n\033[31;1m您输入的错误次数过多,%s 已经被锁定！\033[0m" % username)