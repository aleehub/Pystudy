#对象创建并添加熟悉后，能否在类的实例方法里获取这些熟悉？




class Hero(object):
    """定义一个英雄类，可以移动和攻击"""

    def move(self):
        """实例方法"""

        print("正在前往事发地点...")


    def attack(self):

        print("发出一记强有力的普通攻击....")


    def info(self):
        """ 在类的实例方法中，通过self获取该对象的属性"""

        print(f"英雄{self.name}的生命值{self.hp}")
        print(f"英雄{self.name}的攻击力{self.atk}")
        print(f"英雄{self.name}的护甲值{self.armor}")


taidamier = Hero()

taidamier.name = "taidamier"

taidamier.hp = 2600

taidamier.atk = 450

taidamier.armor = 200


taidamier.info()

taidamier.move()
taidamier.attack()