# 进程的注意点：
#  1.进程之间不共享全局变量
#  2. 主进程会等待所有的子进程执行结束再结束



# 1. 进程之间不共享全局变量
# demo

import multiprocessing
import time

# # 定义全局变量
g_list = list()
#
#
# # 添加数据的任务
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    # 代码执行到此，说明数据添加完成
    print("add_data:", g_list)


def read_data():
    print("read_data", g_list)


if __name__ == '__main__':
    # 创建添加数据的子进程
    add_data_process = multiprocessing.Process(target=add_data)
    # 创建读取数据的子进程
    read_data_process = multiprocessing.Process(target=read_data)

    # 启动子进程执行对应的任务
    add_data_process.start()
    # 主进程等待添加数据的子进程执行完成以后程序再继续往下执行，读取数据
    add_data_process.join()
    read_data_process.start()

    print("main:", g_list)

    # 总结: 多进程之间不共享全局变量


# 进程之间不共享全局变量：
# 如果不同的进程操作一个同名变量，它们分别操作自己的进程里面的全局变量：
# 它们里面的全局变量只不过是名字相同而已。


# 2. 主进程会等待所有的子进程执行结束再结束

# 假如我们现在创建一个子进程，这个子进程执行完大概需要2秒钟，现在让主进程执行0.5秒就退出程序，

# 查看一下执行结果，示例代码如下：

import multiprocessing
import time
#
#
# # 定义进程所需要执行的任务
def task():
    for i in range(10):
        print("任务执行中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    sub_process.start()

    # 主进程延时0.5秒钟
    time.sleep(0.5)
    print("over")
    exit()

    # 总结： 主进程会等待所有的子进程执行完成以后程序再退出

# 说明：
#  通过上面代码的执行结果，我们可以得知：主进程会等待所有的子进程执行结束再结束

# 当我们想结束主进程时，而如果子进程没有结束，我们就不能马上结束主进程：

# 为了处理这种问题，我们可以设置守护主进程或者在主进程退出之前让子进程销毁

# 守护主进程：

#     1 . 守护主进程 ：
#           守护主进程就是主进程退出子进程销毁不再执行

#      2. 子进程销毁
#             子进程执行结束


# demo

import multiprocessing
import time


# 定义进程所需要执行的任务
def task():
    for i in range(10):
        print("任务执行中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 设置守护主进程，主进程退出子进程直接销毁，子进程的生命周期依赖与主进程
    sub_process.daemon = True
    sub_process.start()

    time.sleep(0.5)
    print("over")
    # 让子进程销毁
    # sub_process.terminate()
    # exit()

    # 总结： 主进程会等待所有的子进程执行完成以后程序再退出
    # 如果想要主进程退出子进程销毁，可以设置守护主进程或者在主进程退出之前让子进程销毁

# 小结：
# 1. 为了保证子进程能够正常的运行，主进程会等所有的子进程执行完成以后再销毁，设置守护主进程的目的是主进程退出子进程销毁，不让主进程再等待子进程去执行。
# 2. 设置守护主进程方式： 子进程对象.daemon = True
# 3. 销毁子进程方式： 子进程对象.terminate()

