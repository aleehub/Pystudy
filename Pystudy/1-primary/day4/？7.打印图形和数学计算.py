# 感受函数的嵌套调用
# 感受程序设计的思路，复杂问题分解为简单问题


import time
import os


def a():
    print(".", end=" ", flush=True)

    # end 与 time 不兼容


def b(num):
    for i in range(num):
        time.sleep(0.5)
        a()


b(10)

# time函数运行完，才开始运行printLine

# 写一个函数求三个数的和
# 写一个函数求三个数的平均值


# 求3个数的和
# def sum3Number(a,b,c):
#     return a+b+c # return 的后面可以是数值，也可是一个表达式
#
# # 完成对3个数求平均值
# def average3Number(a,b,c):
#
#     # 因为sum3Number函数已经完成了3个数的就和，所以只需调用即可
#     # 即把接收到的3个数，当做实参传递即可
#     sumResult = sum3Number(a,b,c)
#     aveResult = sumResult/3.0
#     return aveResult
#
# # 调用函数，完成对3个数求平均值
# result = average3Number(11,2,55)
# print("average is %d"%result)
