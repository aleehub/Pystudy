# 在创建对象的时候，就拥有某些属性

class Hero(object):


   # Python的类里童工的，两个下划线开始，两个下划线结束的方法，就是魔法方法，__init__()就是一个魔法方法，通常用来做属性初始化或者赋值操作。
   # 如果类里面没有写__init__方法，Python会自动创建，但是不会执行任何操作，
   # 如果为了能够在完成自己想要的功能，可以自己定义__init__方法
   # 所以一个类里无论自己是否编写__init__方法，一定有__init__方法

   # 在程序中 不能有多行注释


    def __init__(self):

        self.name = "taidamier"

        self.hp = 2600

        self.atk = 450

        self.armor = 200



    def move(self):

        print("正在前往事发地点...")

    def attack(self):

        print("发出一招强力的普通攻击")


    def info(self):
        """ 在类的实例方法中，通过self获取该对象的属性"""

        print(f"英雄{self.name}的生命值{self.hp}")
        print(f"英雄{self.name}的攻击力{self.atk}")
        print(f"英雄{self.name}的护甲值{self.armor}")


taidamier = Hero()

taidamier.info()

taidamier.move()

taidamier.attack()

