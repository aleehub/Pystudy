# 根据已经定义的类去创建一个或者多个对象

# 创建对象的格式为：

# 对象名1 = 类名()
# 对象名2 = 类名()
# 对象名3 = 类名()

# 创建对象demo:

class Hero(object):
    """info是一个实例方法，类对象可以调用实例方法，实例方法的第一个参数一定是self"""


    def info(self):
        """当对象调用实例方法时，Python会自动将对象本身的引用做为参数，
        传递到实例方法的第一个参数self里"""
        print(self)
        print("self各不同，对象是出处")



taidemier = Hero()

taidemier.info()

print(taidemier)

print(id(taidemier))