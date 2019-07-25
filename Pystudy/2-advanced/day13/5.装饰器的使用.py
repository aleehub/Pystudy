# 装饰器的作用

# 1.装饰器的使用场景

#   1.函数执行时间的统计

#   2.输出日志信息


# 2. 装饰器实现已有函数执行时间的统计

import time


# 装饰器函数

def get_time(func):

    def inner():

        begin = time.time()

        func()

        end = time.time()

        print("函数执行花费%f"%(end-begin))


    return inner


@get_time

def func():

    for i in range(100000):
        print(i)



func()