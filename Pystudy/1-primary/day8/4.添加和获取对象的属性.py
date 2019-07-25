#
class Hero(object):
    """定义了一个英雄类，可以移动和攻击"""

    def move(self):
        """实例方法"""

        print("正在前往事发地点")


    def attack(self):

        """实例方法"""

        print("发出一招强力的普通攻击")



taidamier = Hero()


taidamier.name = "泰达米尔"

taidamier.hp = 2600

taidamier.atk = 450

taidamier.armor = 200


print(f"英雄{taidamier.name}的生命值{taidamier.hp}")

print(f"英雄{taidamier.name}的攻击力{taidamier.atk}")

print(f"英雄{taidamier.name}的护甲值{taidamier.armor}")

taidamier.move()

taidamier.attack()