# 能够知道定义装饰器的语法格式

# 1.装饰器的定义

# 就是给已有函数增加额外功能的函数,他本质就是一个闭包函数


# 装饰器的功能特点:

#   1.不修改已有函数的源代码
#   2.不修改已有函数的调用方式
#   3. 给已有函数增加额外的功能

# demo

# 添加一个登录验证的功能

# def check(fn):
#
#     def inner():
#         print("请先登录.....")
#
#         fn()
#
#
#     return inner
#
# def comment():
#
#     print("请登录")
#
# comment = check(comment)
#
# comment()

# 装饰器的基本雏形

# def decorator(fn) : # fn : 目标函数

#   def inner():

# """执行函数之前"""

#       fn()   # 执行被装饰的函数

#   '''执行函数之后'''

#   return inner

# 闭包函数有且只有一个参数,必须是函数类型,这样定义的函数才是装饰器.
# 写代码要遵循开发封闭原则,它规定已经实现的功能不允许被修改,但可以被扩展.

# 装饰器的语法糖写法

# 添加一个登录验证的功能

def  check(fn):

    print("装饰器函数执行了")

    def inner():
        print("请先登录")

        fn()

    return inner


# 使用语法糖方式来装饰函数

@check  # @check 等价于comment = check(comment)


def comment():
    print("发表评论")




comment()


# 小结:

#   装饰器本质就是一个闭包函数,它可以对已有函数进行额外的功能扩展.

#   装饰器的语法格式:

#