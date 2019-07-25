# 1. 捕获异常

# demo

try:            # 将可能会产生异常的代码，放在try中。
    print('-----test--1---')
    open('123.txt','r')         # 当出现异常后，后面的语句不会执行。
    print('-----test--2---')

except  IOError:  # 针对单个错误，只当出现这个错误时，才捕获，其他错误不捕获。
                  #  当要针对所有错误时，直接用except

     pass         #如果产生异常时，处理的方法




# 此时程序看不到任何错误，因为用Except 捕获了 IOE异常，并添加了处理的方法

# pass 表示实现了相应的实现 ，但什么也不做，如果把pass改为print语句，那么就会输出其他信息


# 2.捕获多个异常


#coding=utf-8
try:
    print('-----test--1---')
    open('123.txt','r') # 如果123.txt文件不存在，那么会产生 IOError 异常
    print('-----test--2---')
    print(num)# 如果num变量没有定义，那么会产生 NameError 异常

except (IOError,NameError):
    #如果想通过一次except捕获到多个异常可以用一个元组的方式

  pass  # 如果只捕获了异常，而不处理就会出现编译错误


# 当捕获了多个异常时，可以把要捕获了异常的名字，放到except后，并使用元组的方式进行存储
# 当不写异常名字时，即代表捕获所有异常

# 3. 捕获异常的信息描述

#  在捕获异常时，可以将捕获的异常信息进行存储

#  demo

try:
    print(a)

except NameError as result:

    print(result)


# 4. 捕获所有的异常


# 如果不存储异常信息，可以将except 后的异常省略
# 如果要存储异常信息

# demo

try :

    print(a)

except Exception as result:

    print(result)


# 5.else

# 放在try 中的可能会出现的异常的语句， 如果没有出现异常，则会则会执行else语句下内容

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
else:
    print('没有捕获到异常，真高兴')


# 6. try..finally

# 在程序中，如果一个段代码必须要执行，即无论异常是否产生都要执行，那么此时就需要使用finally。 比如文件关闭，释放锁，把数据库连接返还给连接池等


import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        #如果在读取文件的过程中，产生了异常，那么就会捕获到
        #比如 按下了 ctrl+c
        pass
    finally:
        f.close()
        print('关闭文件')
except:
    print("没有这个文件")


# test.txt文件中每一行数据打印，但是我有意在每打印一行之前用time.sleep方法暂停2秒钟。这样做的原因是让程序运行得慢一些。在程序运行的时候，按Ctrl+c中断（取消）程序。
#
# 我们可以观察到KeyboardInterrupt异常被触发，程序退出。但是在程序退出之前，finally从句仍然被执行，把文件关闭。