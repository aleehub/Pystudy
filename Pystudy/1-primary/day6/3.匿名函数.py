# 匿名函数的概念
# 匿名函数即没有名字的函数

# 语法格式： lanbda [形参1]，[形参2]，：[单行表达式]


# 不带参数
my_fun = lambda: 10 + 20
# 带参数
my_add = lambda a, b: a + b
print(my_add(1, 2))

# 匿名函数中不能使用 if 语句、while 循环、for 循环, 只能编写单行的表达式，或函数调用, 普通函数都可以.
# 匿名函数中返回结果不需要使用 return, 表达式的运行结果就是返回结果, 普通函数返回结果必须 return.
# 匿名函数中也可以不返回结果. 例如: lambda : print('hello world')
