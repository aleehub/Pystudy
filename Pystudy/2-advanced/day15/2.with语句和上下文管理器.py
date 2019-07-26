# # 上下文管理器的两种方式
#
# # with语句的使用
#
# # demo
#
# # 1.以写的方式打开文件
#
# f = open("1.txt", "w")
#
# # 2. 写入文件内容
#
# f.write("hello world")
#
# # 3.关闭文件
#
# f.close()
#
# # 文件使用后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
#
# # 当文件被读的方式打开，却往里面写入内容就会引发错误
#
# # 由于文件读写会引发IOError,一旦出错，后面的f.close()就不会调用。
# # 为了保证无论是否出错都能正确的关闭文件，我们可以使用try...finally来解决
#
# try:
#     #   1.以读的方式打开文件
#     f = open("1.txt", "r")
#
#     f.write("xxxx")
#
#
# except Exception as e:
#
#     print("文件操作错误")
#
#
# finally:
#
#     # 3.关闭文件
#
#     f.close()

# python 为什么要关闭文件？
# 1. 关闭文件可以近似看做我们的电脑的刷新功能，关闭文件后，文件内容才会同步至磁盘
# 2.linux系统中，每个进程打开文件数量是有限的，如果不关闭，资源释放就要等到垃圾回收完成
# 3.打开太多文件不关闭，有可能导致资源耗尽，无法打开新的文件


# with 语句执行完成以后自动调用关闭文件操作，及时出现也会自动调用关闭文件操作
# demo
with open("1.txt","w") as file:

    file.write("hello world")


# 上下文管理器

# 定义一个file类

class File(object):

    # 初始化方法
    def __init__(self,file_name,file_model):

        # 定义变量保存文件名和打开模式

        self.file_name = file_name
        self.file_model = file_model


    # 上文方法

    def __enter__(self):

        print("进入上文方法")

        # 返回文件资源
        self.file = open(self.file_name,self.file_model)

        return self.file


    # 下文方法

    def __exit__(self, exc_type, exc_val, exc_tb):

        print("执行下文方法")

        self.file.close()


if __name__ == '__main__':

    with File("1.txt","r") as file:

        file_data = file.read()

        print(file_data)


# 上下文管理器的另一种实现方式

# 假如想要让一个函数成为上下文管理器，Python 还提供了一个@contextmanager的装饰器，更加一部简化了上下文管理器的实现方式，通过yield将函数分割成两部分


# 导入装饰器

from contextlib import contextmanager


# 装饰器装饰好函数，让其称为一个上下文文件管理对象

@contextmanager
def my_open(path,mode):

    try:

        file = open(path,mode)

        yield file

    except Exception as e:

        print(e)

    finally:

        print("over")
        file.close()


# 使用with 语句

with my_open("out.txt","w") as f:

    f.write("hello,the simplest context manager")




