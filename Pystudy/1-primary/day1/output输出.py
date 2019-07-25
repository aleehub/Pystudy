# 普通的输出

print("1.这是一个普通的输出")

# 格式化输出

# 单个字符
age1 =10

print("我今年%d岁" %age1)


# 多个字符,当多个字符时，组成一个元组。
age2=11
name="liya"

print("i am %d years old,my name is %s" %(age2,name))

'''

常用的格式符号：
1.%c    字符
2.%s    字符串
3.%d    有符号十进制整数
4.%u    无符号整数
5.%o    八进制整数
6.%x    十六进制整数（小写字母0x)
7.%X    十六进制整数（大写字母0X）
8.%f    浮点数
9.%e    科学计数法  小写
10.%E   科学计数法   大写

'''

# 换行输出

print("123456789------")
print("1234567890\n--------")

#练一下

#1
name="小明"
print("my name is %s" %name)
print(f"my name is {name}")

#2
student_no =1

print("my student id is %06d" %student_no)

#3

price = 9
weight = 5
money = price*weight

print("苹果单价是%.02f元/斤,购买了%.02f斤,需要支付%.02f元" %(price,weight,money))

#4

scale=10

print("数据比例是%.02f%%" %scale)

#5
name = "itheima"
QQ = 462523421
phone = 13358254839
address ="广东省深圳市"

print("==========我的名片==========")
print(f"姓名：{name}")
print(f"QQ：{QQ}")
print(f"手机号：{phone}")
print(f"公司地址：{address}")
print("===========================")
