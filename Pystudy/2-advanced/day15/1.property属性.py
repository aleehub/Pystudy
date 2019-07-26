# property 属性

# property属性的 定义方式

# 1. propery属性就是负责把一个方法当做属性进行使用

# 定义property属性有两种方式

# 1. 装饰器方式
# 2.类属性方式

#demo

class Person(object):

    def __init__(self):

        self.__age = 0


    #装饰器方式的property,把age方法当做属性使用，表示当获取属性时会执行下面修饰的方法

    @property
    def age(self):

        return self.__age

    # 把age方法当做属性使用，表示当设置属性时会执行下面修饰的方法

    @age.setter
    def age(self,new_age):

        if new_age >= 150:
            print("成精了")

        else:

            self.__age = new_age


# 创建 person

p = Person()

print(p.age)

p.age = 100

print(p.age)

p.age = 1000

# @property 表示把 方法当做属性使用，表示当获取属性时会执行下面修饰的方法
# @方法名。setter 表示把方法当做属性使用，表示当设置属性时会执行下面修饰的方法
# 装饰器方式的property属性的方法名一定要一样
# 类属性方式

class Person(object):

    def __init__(self):

        self.__age = 0


    def get_age(self):
        """当获取age属性的时候会执行该方法"""
        return self.__age

    def set_age(self,new_age):
        """当设置age属性的时候会执行该方法"""

        if new_age >= 150:
            print("成精了")

        else:
            self.__age = new_age



    # 类属性方式的property属性

    age = property(get_age,set_age)



# 创建person
p = Person()

print(p.age)

p.age = 100

print(p.age)

p.age = 1000


# 代码说明：
# property 的参数说明：

# 第一个参数时获取属性时要执行的方法
# 第二个参数是设置属性时要执行的方法

# 小结
# 定义property 属性有两种方式
    #1. 装饰器方式
    #2. 类属性方式
# 装饰器方式:
# @property 修饰获取值的方法
# @方法名.setter 修饰设置值的方法
# 类属性方式:
# 类属性 = property(获取值方法, 设置值方法)

