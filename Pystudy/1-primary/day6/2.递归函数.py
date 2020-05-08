# 什么是递归函数
# 一个函数可以调用其他函数
# 当这个函数调用本身的话就是递归函数

def calNum(num):
    if num >= 1:

        result = num * calNum(num - 1)

    else:
        result = 1

    return result


ret = calNum(3)

print(ret)
