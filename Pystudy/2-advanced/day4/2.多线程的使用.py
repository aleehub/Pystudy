# 多线程的使用
# 学习目标
# 能够使用多线程完成多任务

# 1. 导入线程模块
#   导入线程模块
#   import threading

# 2. 线程类Thread参数说明
# Thread([group [, target [, name [, args [, kwargs]]]]])
# group: 线程组，目前只能使用None
# target: 执行的目标任务名
# args: 以元组的方式给执行任务传参
# kwargs: 以字典方式给执行任务传参
# name: 线程名，一般不用设置

# 3. 启动线程
# 启动线程使用start方法

# 4. 多线程完成多任务的代码

import threading
import time

def sing():

    for i in range(5):

        print("唱歌中...")

        time.sleep(0.2)


def dance():

    for i in range(5):

        print("跳舞中...")

        time.sleep(0.2)

if __name__ == '__main__':

    sing_thread = threading.Thread(target=sing)

    dance_thread = threading.Thread(target=dance)

    sing_thread.start()

    dance_thread.start()

# 5. 小结
# 导入线程模块
# import threading
# 创建子线程并指定执行的任务
# sub_thread = threading.Thread(target=任务名)
# 启动线程执行任务