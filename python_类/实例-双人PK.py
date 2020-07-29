import random


class Role:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def tong(self, enemy):
        """
        捅：减少10血
        :return:
        """
        print("{}捅了{}一刀".format(self.name, enemy.name))
        enemy.hp -= 10
        pass

    def kan(self, enemy):
        """
        砍：减少15血
        :return:
        """
        print("{}砍了{}一刀".format(self.name, enemy.name))
        enemy.hp -= 15
        pass

    def heyao(self):
        """
        喝药:加10血
        :return:
        """
        print("{}喝了一瓶药，恢复10生命".format(self.name))
        self.hp += 10
        pass

    def __str__(self):
        """
        打印当前状态
        打印当前状态
        :return:
        """
        return "{}还剩{}生命".format(self.name, self.hp)
        pass


p1 = Role("东方不败")
p2 = Role("独孤求败")
print("**********************")
while p1.hp and p2.hp:
    if p1.hp > 0:
        p1.tong(p2)
        print(p1)
        print(p2)
        print("**********************")
    if p2.hp > 0:
        p2.kan(p1)
        print(p1)
        print(p2)
        print("**********************")
    if p1.hp > 0 and p2.hp > 0:
        p1.heyao()
        print(p1)
        print(p2)
        print("**********************")

print("{}获胜".format(max(p1, p2, key=lambda p: p.hp).name))


