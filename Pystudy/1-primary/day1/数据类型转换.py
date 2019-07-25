'''
1. int(x[,base])  base: 基于什么进制转换,默认10进制
2. float()
3. complex(real[,imag])
4.str()
5.repr()
6.eval()
7.tuple()
8.list()

9.chr() 将一个整数转换为Unicode字符
10.ord() 将一个字符转换成它的ASCII整数值

11.不同进制数值的转换
    1.hex() 16进制
    2.oct() 8进制
    3.bin() 2进制
'''

str1="10"

num1 = int(str1)
print(num1)

num2 = int(str1,8)
print(num2)

num3 = int(str1,16)
print(num3)


# print()默认打印出的数以10进制的形式显示出来，即使打印一个其他进制的数.
# 定义一个二进制数 0b 开头表示二进制数
binary1 = 0b111
print(binary1)

# 定义一个八进制数 0o 开头表示八进制数
oct1=0o66
print(oct1)


# 定义一个十六进制数 0x 开头表示16进制数
hex1 = 0x0f
print(hex1)


# 万能方法 eval() 将字符串转换成它本来的类型

#ASCII码  A-Z  65~90   a-z 97~122