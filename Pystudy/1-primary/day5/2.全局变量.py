# 全局变量
# 如果一个变量，既能在一个函数中使用，也能在其他的函数中使用，这样的变量就是全局变量
# 在函数外边定义的变量叫做全局变量
# 全局变量能够在所有的函数中进行访问

# 全局变量与局部变量同名问题

# 局部定义一个与全局变量相同名字的变量时。不会对全局变量进行改变


# 当在函数内部想修改全局变量时，在函数内部 变量前加入globe关键字

# demo

a = 100


def test1():
    global a

    print(a)

    a = 200

    print(a)


def test2():
    print(a)


test1()
test2()

# 如果在函数中出现global全局变量的名字，那么这个函数中即使出现和全局变量相同的变量名=数据
# 也理解对全局变量进行改变

# 如果要对多个个全局变量进行修改
# global a,b

# demo

a = 100
b = 20


def test1():
    global a, b
    print(a)
    a = 200
    print(a)


def test2():
    print(a)


test1()
test2()
