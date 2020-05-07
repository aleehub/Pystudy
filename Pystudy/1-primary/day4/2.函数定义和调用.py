# 定义函数

# def 函数名():
#     代码


# demo

def printInfo():
    print('------------------------------------')
    print('         人生苦短，我用Python')
    print('------------------------------------')


# 调用函数
# 定义了函数后，就相当于有了一个具有某些功能的代码，想让这些diamante能够执行，需要调用它

# 通过函数名来调用

# deno

printInfo()


# 每次调用函数时，函数都会从头开始执行，当这个函数的代码执行完毕后，意味着调用结束了
# 当然了如果函数执行到了return 也会结束函数

# 练一练
# 定义一个函数，能够输出自己的姓名和年龄，并且调用这个函数让它执行

def myinfo():
    print("my name is liyuhang")

    print("my age is 25 years old")

    printInfo()


myinfo()
