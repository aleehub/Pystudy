class Hero(object):

    def __init__(self,name,skill,hp,atk,armor):
        """ __init__()方法，用来做变量初始化 或赋值操作"""

        self.name = name

        self.skill = skill

        self.hp = hp

        self.atk = atk

        self.armor = armor


    def move(self):

        print(f"{self.name}正在前往事发地点")


    def attack(self):
        """实例方法"""
        print("发出了一招强力的%s..." % self.skill)

    def info(self):
        print("英雄 %s 的生命值 :%d" % (self.name, self.hp))
        print("英雄 %s 的攻击力 :%d" % (self.name, self.atk))
        print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))


# 实例化英雄对象时，参数会传递到对象的__init__()方法里
taidamier = Hero("泰达米尔", "旋风斩", 2600, 450, 200)
gailun = Hero("盖伦", "大宝剑", 4200, 260, 400)


print(gailun)

print(taidamier)

print(id(taidamier))
print(id(gailun))

# 不同对象的属性值的单独保存
print(id(taidamier.name))
print(id(gailun.name))

# 同一个类的不同对象，实例方法共享
print(id(taidamier.move()))
print(id(gailun.move()))


# 通过一个类，可以创建多个对象，就好比通过一个模具创建多个实体一样

"""__init__(self)中，默认有一个参数名字为self，如果在创建时传递了两个实参，那么__init__(self) 中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)"""

# 在内部获取属性和实例方法，通过self获取；
# 在类外部获取属性和实例方法，通过对象名获取
# 如果在一个类有多个对象，每个对象的属性是各自保存的 ，都有各自独立的地址
# 但是实例方法是所有对象共享的，只占用一份内存空间。
# 类会通过self来判断是哪个对象调用了实例方法



