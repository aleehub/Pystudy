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



