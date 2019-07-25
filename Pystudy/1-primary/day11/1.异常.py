#  异常

# demo
print
'-----test--1---'
open('123.txt', 'r')
print
'-----test--2---'


# Traceback (回溯)(most recent call last)最后一次通话:
#   File "/home/python/Desktop/Pystudy/1-primary/day11/1.异常.py", line 6, in <module>
#     open('123.txt', 'r')
# FileNotFoundError: [Errno 2] No such file or directory: '123.txt'


# 打开一个不存在的文件123.txt , 当找不到123.txt 文件时, 就会抛给我们一个IOError类型的错误，N


# 异常
#  当Python 检测到一个错误时，解释器就无法继续执行了，反而会出现一些错误的提示，这就是所谓的异常


