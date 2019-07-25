# 能够使用通用的装饰器

# 1. 装饰带有参数的函数

# 添加输出日志的功能

# def logging(fn):
#
#     def inner(num1,num2):
#
#         print("---正在努力计算中---")
#
#         fn(num1,num2)
#
#     return inner
#
#
#
# @logging
#
# def sum_num(a,b):
#
#     result = a + b
#
#     print(result)
#
# sum_num(1,2)

# 2. 装饰带有返回值的函数

# 添加输出日志的功能

# def logging(fn):
#
#     def inner(num1,num2):
#
#         num1 = 2
#         num2 = 3
#         print("--正在努力计算")
#
#         result = fn(num1,num2)
#
#         return result
#
#     return inner
#
#
# @logging  # sun_num = logging(sum_num)
# def sum_num(a,b):
#
#     result = a + b
#
#     return result
#
# result = sum_num(1,2)
#
# # 传递过程
#
# # 1. 先定义装饰器
# # 2. 定义被装饰函数
# # 3. 语法糖装饰被装饰函数
# # 4. 参数被传递到内嵌函数形参上
# # 5. 内嵌函数的参数再传递到被装饰函数
#
# print(result)
#
# print(sum_num)
# print()

# 打印方法名 显示方法对象
# 打印方法   显示返回数值,如果没有对象 为NoneType
# 打印被语法糖修饰的方法名,为内嵌函数


# 3.装饰带有不定长参数的函数
# 添加输出日志的功能
# def logging(fn):
#     def inner(*args,**kwargs):
#         print("--正在努力计算--")
#         fn(*args,**kwargs)
#
#
#     return inner
#
# # logging
#
# def sum_num(*args,**kwargs):
#     result = 0
#
#     for value in args:
#
#         result += value
#
#
#     for value in kwargs.values():
#         result += value
#
#
#     print(result)
#
# sum_num(1,2,a=10)


# 通用装饰器

# 添加输出日志的功能

def logging(fn):

    def inner(*args,**kwargs):

        print("--正在努力计算--")
        result = fn(*args,**kwargs)

        return result


    return inner

#使用语法糖装饰函数

@logging
def sum_num(*args,**kwargs):
    result = 0

    for value in args:
        result += value

    for value in kwargs.values():
        result += value

    return result


@logging

def subtraction(a,b):
    result = a - b

    print(result)

result = sum_num(1,2,a=10)

print(result)

subtraction(4,2)

