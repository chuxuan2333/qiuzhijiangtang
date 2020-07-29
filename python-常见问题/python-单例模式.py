
# 单例模式:确保一个类在系统运行期间只有一个实例对象
# 应用场景:日志，网站计数器，数据库连接池，Windows资源管理器，系统回收站，


class User(object):

    # 单例模式实现
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            # print(cls._instance)
        return cls._instance


user1 = User()
user2 = User()
print(user1 is user2)
print(id(user1) == id(user2))
print(id(user1), id(user2))

