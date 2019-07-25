
# 导入进程包
import multiprocessing


# multiprocessing  模块中有process类

# Process类的说明

# Process: 参数列表
# group     进程组
# target    执行目标任务名
# name      进程名
# args      以元组的方式给任务传参

# Process 创建的实例对象的常用方法:

# start()       启动子进程实例
# join()        等待子进程执行结束
# terminate()   不管任务是否完成,立即终止子进程

# demo:

import time

def dance():

    for i in range(100):

        print("跳舞中...")
        time.sleep(1)

def sing():

    for i in range(100):
        print("唱歌中...")
        time.sleep(1.5)

if __name__ == '__main__':

    # 创建跳舞的子进程
    # group: 表示进程组，目前只能使用None
    # target: 表示执行的目标任务名(函数名、方法名)
    # name: 进程名称, 默认是Process-1, .....


    # 创建一个multiprocessing模块中,Process类的实例
    dance_process = multiprocessing.Process(target=dance,name="myprocess1")

    sing_process = multiprocessing.Process(target=sing)

    # name 是当前进程的别名,当没有定于时,就会默认为Process-N(N为从1开始的整数)

    print(dance_process.name) #有定义,此时名字为没有myprocess1

    print(sing_process.name)  # 没有定义,此时名字为Process-2


    # Process类中有start()方法,用于启动进程
    dance_process.start()


    sing_process.start()


# 小结:

#   1. 导入进程包:
#       import multiprocesssing

#   2. 创建子进程:
#       process_name = multiprocessing.Process(target = taskName , name = youProcessName)

#   3. 启动子进程执行任务
#       process_name.start()






