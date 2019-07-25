# 如何获取进程的编号
# 根据获得的进程编号来结束当前进程

# 1. 获取进程编号的目的:
#    1.获取进程编号的目的是验证主进程和子进程的关系,可以得知子进程是有哪个主进程创建出来的
#    2. 获取进程编号的两种操作
#       1.获取当前进程编号
#       2.获取当前父进程编号

# 2. 获取当前进程编号
# os.getpid() 表示获取当前进程编号

# demo

# import multiprocessing
#
# import time
#
# import os
#
# def dance():
#
#     # 获取当前进程编号
#     dancePid = os.getpid()
#     print("dancePId:",dancePid)
#     # 获取当前进程
#     print("dance:",multiprocessing.current_process())
#
#     for i in range(5):
#
#         print("跳舞中...")
#
#         time.sleep(0.2)
#
#
# def sing():
#
#     # 获取当前进程编号
#     singPid = os.getpid()
#
#     print("singPId:",singPid)
#     # 获取当前进程
#     print("sing:",multiprocessing.current_process())
#
#     for i in range(5):
#
#         print("唱歌中...")
#
#         time.sleep(0.2)
#
#
# if __name__ == '__main__':
#
#     dance_process = multiprocessing.Process(target=dance)
#
#     sing_process = multiprocessing.Process(target=sing)
#
#     print("main:",os.getpid())
#
#     dance_process.start()
#
#     sing_process.start()


# 3. 获取当前父进程编号

# os.getppid()

import multiprocessing

import time

import os

def danceNew():
    # 获取当前进程编号
    print("dancePId:", os.getpid())
    # 获取当前进程
    print("dance:", multiprocessing.current_process())
    # 获取父进程的编号
    print("dance父进程pid:",os.getppid())


    for i in range(5):

        print("跳舞中....")

        time.sleep(0.2)

        os.kill(os.getpid(),9)



def singNew():

    print("singPId:", os.getpid())

    print("sing:", multiprocessing.current_process())

    print("sing父进程pid:", os.getppid())

    for i in range(5):
        print("唱歌中....")

        time.sleep(0.2)

if __name__ == '__main__':

    print("main:", os.getpid())

    print("main:", multiprocessing.current_process())

    dance_process = multiprocessing.Process(target=danceNew)

    sing_process = multiprocessing.Process(target=singNew)

    dance_process.start()

    sing_process.start()

# 小结:
#  1.获取当前进程编号
#       os.getpid()
#  2.获取当前父进程编号
#       os.getppid()
#  3.强制结束当前进程
#       os.kill(pid,9)