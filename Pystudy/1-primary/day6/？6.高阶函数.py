# map 函数
# map(function,args)
# args中的每个元素都会被当做参数传入到function中


my_list = [1, 2, 3, 4, 5]


def f(x):
    return x ** 2


result = map(f, my_list)
print(type(result), result, list(result))


# reduce
# reduce 函数会对参数序列中元素进行累计
# 函数将一个数据集合中的所有数据进行下列操作:
#
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作.
# 得到的结果再与第三个数据用 function 函数运算, 最后得到一个结果.

import functools

my_list = [1, 2, 3, 4, 5]


def f(x1, x2):
    return x1 + x2


result = functools.reduce(f, my_list)
print(result)


# filter
# filter() 函数用于过滤序列, 过滤掉不符合条件的元素, 返回一个 filter 对象, 如果要转换为列表, 可以使用 list() 来转换.
#
# 该接收两个参数, 第一个为函数, 第二个为序列, 序列的每个元素作为参数传递给函数进行判, 然后返回 True 或 False, 最后将返回 True 的元素放到新列表中.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def f(x):
    return x % 2 == 0


result = filter(f, my_list)
print(list(result))