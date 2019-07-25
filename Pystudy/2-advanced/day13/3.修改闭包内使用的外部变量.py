# 能够知道修改闭包内使用的外部变量所需要的关键字

# 1. 修改闭包内使用的外部变量

# 修改闭包外使用的外部变量的错误示例:

# 定义一个外部函数

# def func_out(num1):
#
#     # 定义一个内部函数
#
#     def func_inner(num2):
#
#        # 这里本意想要修改外部num1的值,实际上是在内部函数定义了一个局部变量num1
#
#         num1 = 10
#
#        # 内部函数使用了外部函数的变量(num1)
#
#         result = num1 + num2
#
#         print("结果是:",result)
#
#     print(num1)
#
#     func_inner(1)
#
#     print(num1)
#
#     return func_inner
#
# f = func_out(1)
#
# f(2)

# 修改闭包内使用的外部变量的正确示例:

# 定义一个外部函数
def func_out(num1):

    # 定义一个内部函数
    def func_inner(num2):

        # 这里本意想要修改外部num1的值,实际是在内部函数定义一个局部变量num1

        nonlocal num1  # 告诉解释器,此处使用的是外部变量a

        num1 = 10

        # 内部函数使用了外部函数的变量(num1)

        result = num1 + num2

        print("结果是:",result)


    print(num1)
    func_inner(1)

    print(num1)


    print(num1)

    return func_inner

f = func_out(1)

f(2)

# 修改内使用的外部函数变量使用nonlocal关键字来完成

