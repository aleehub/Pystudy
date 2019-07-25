# 使用全局变量

g_num = 0

def test1():
    global g_num
    # 将处理结果存储到全局变量g_num中.....
    g_num = 100

def test2():
    # 通过获取全局变量g_num的值, 从而获取test1函数处理之后的结果
    print(g_num)

# 1. 先调用test1得到数据并且存到全局变量中
test1()

# 2. 再调用test2，处理test1函数执行之后的这个值
test2()


# 使用函数的返回值，参数

def test1():
    # 通过return将一个数据结果返回
    return 50


def test2(num):
    # 通过形参的方式保存传递过来的数据，就可以处理了
    print(num)


# 1. 先调用test1得到数据并且存到变量result中
result = test1()

# 2. 调用test2时，将result的值传递到test2中，从而让这个函数对其进行处理
test2(result)


# 函数嵌套使用

def test1():
    # 通过return将一个数据结果返回
    return 20

def test2():
    # 1. 先调用test1并且把结果返回来
    result = test1()
    # 2. 对result进行处理
    print(result)

# 调用test2时，完成所有的处理
test2()
