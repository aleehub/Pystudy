# 写数据
# write() 使用write() 可以完成向文件写入数据

# demo

f = open('test.txt','w')

f.write("hello world,i am here!")

f.close()

# 如果文件不存在，那么就创建，如果存在那么就先清空，然后写入数据




# 读数据
# read(num) 表示从文件中读取的数据的长度（单位字节），如果没有传入num,那么就表示读取文件中所有数据
f = open("test.txt","r")  # open文件时，如果只有读，则可以将"r"省略，即只写open("test.txt")
content = f.read(5)
print(content)
print("-"*30)
content=f.read()   # 如果文件没有关闭，则会从上次读取的位置继续读取
print(content)
f.close()


# 读数据 readlines
# readlines 可以按照行的方式把整个文件的 内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素

f = open("test.txt","r")

content = f.readlines()

print(type(content))

print(content)

for i in content:
    print(i)

f.close()


# 读数据 readline  只读取一行

f = open("test.txt")

content = f.readline()

print(content)







