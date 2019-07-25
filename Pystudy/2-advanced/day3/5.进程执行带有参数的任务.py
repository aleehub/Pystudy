# 进程执行带有参数的任务

# 1.前面使用的进程执行的任务是没有参数的,但执行的进程有参数时,该如歌传参.
#   Process类执行任务并给任务传参有两种方式:
#       1. args 表示以元组的方式给执行任务传参
#       2. kwargs 表示以字典方式给执行任务传参


# 2. args 的使用

import multiprocessing
import time

# def task(num):
#
#     for i in range(num):
#         print(f"任务执行了第{i+1}次")
#         time.sleep(0.2)
#     else:
#         print("任务执行完成")
#
# if __name__ == '__main__':
#
#     task_process = multiprocessing.Process(target=task,args=(10,))
#
#     task_process.start()


# 3. kwargs 的使用

import multiprocessing
import time

def task(num):

    for i in range(num):
        print(f"任务执行了第{i+1}次")
        time.sleep(0.2)
    else:
        print("任务执行完成")

if __name__ == '__main__':

    # kwargs 以字典的形式来传递变量
    task_process = multiprocessing.Process(target=task, kwargs={"num":10})

    task_process.start()


# 小结:
#   1.元组方式传参(args): 元组方式传参一定要和参数的顺序保持一致。
#   2.字典方式传参(kwargs): 字典方式传参字典中的key一定要和参数名保持一致。