# 1. 现实的继承，继承一般指的是子女继承父辈的财产，如下图

# 2. 程序中的继承

# 程序中，继承描述的是多个类之间的所属关系

#  如果一个类里面的属性和方法可以复用，则可以通过继承的方式，传递到类B里、

# 类A就是基类；也叫作父类；类B就是派生类，也叫作子类

# 父类

class A(object):

    def __init__(self):

        self.num = 10


    def print_num(self):

        print(self.num+ 10)


class B(A):

    pass


b = B()

print(b.num)

b.print_num()