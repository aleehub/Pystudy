# 子类重写父类同名属性和方法

class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"

    def make_cake(self):
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)


class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)



class Prentice(School, Master):  # 多继承，继承了多个父类

    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"

    def make_cake(self):
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)



damao = Prentice()

print(damao.kongfu)

damao.make_cake()

print(Prentice.__mro__)  # 魔法方法__mro__ 是类的方法，对象没有这个属性


