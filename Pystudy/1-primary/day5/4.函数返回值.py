# 讨论 ： 如何返回多个返回值

# return:当使用return时，return下面的语句不会再执行
# return 有一个隐藏功能就是结束函数


# 一个函数返回多个数据的方式

def divid(a, b):
    shang = a//b
    yushu = a%b
    return shang, yushu  #默认是元组

result = divid(5, 2)
print(result)  # 输出(2, 1)


# 当返回多个值时，返回的整体默认是一个元组

def demo():
    s ={}
    ss =[]

    return s,ss

print(demo())

# return 后面可以是元组，列表，字典，只要是能够存储多个数据的类型，就可以一次性返回多个数据

