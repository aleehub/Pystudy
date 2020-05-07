# 在函数中调用其他函数


def testB():
    print('---- testB start----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end----')


def testA():
    print('---- testA start----')
    testB()
    print('---- testA end----')


testA()

# 在函数中又调用另外一个函数，就是所谓的函数调用

# 如果在函数A中，调用另外一个函数B,那么先把函数B中的任务都执行完毕之后才会回到上次函数A执行的位置
