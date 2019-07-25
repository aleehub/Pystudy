# 故事情节：煎饼果子老师傅在煎饼果子界摸爬滚打几十年，拥有一身精湛的煎饼果子技术，并总结了一套"古法煎饼果子配方"。

#  可是老师傅年迈已久，在嗝屁之前希望把自己的配方传承下去，于是老师傅把配方传给他的徒弟大猫...


# 定义一个Master类

class Master(object):

    def __init__(self):

        self.kongfu = "古法煎饼果子配方"


    def make_cake(self):

        print(f"按照{self.kongfu}制作了了一个煎饼果子")



class Prentice(Master):

    pass


# laoli = Master()
#
# print(laoli.kongfu)
#
# laoli.make_cake()


damao = Prentice()  # 创建子类实例对象

print(damao.kongfu) #　子类对象可以直接使用父类的属性

damao.make_cake()   # 子类对象可以直接使用父类的方法

# 虽然子类没有定义__init__方法初始化属性，也没有定义实例方法，但是父类有。所以只要创建子类的对象，就默认执行了那个继承过来的__init__方法

# 子类在继承的时候，在定义类时，小括号()中为父类的名字
# 父类的属性、方法，会被继承给子类

 





