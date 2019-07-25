# 变量的几种类型

'''
1.数值型
    1.int 整型
    2.long 长整型
    3.float 浮点型
    4.complex 复数型
2.布尔类型
    首字母要大写
    1.True
    2.False
3.字符串
4.列表
5.Tuple（元组）
6.Dictionary（字典）
'''

num1=2
bool1=True
str1="hello world！"
list1=[1,2,3]
tuple1=(1,2,3)
dic1={"a":1,"b":2,"c":3}
# 不需要去主动说明变量的类型
# 当给一个变量赋值时，赋的什么值就是什么类型
print(type(num1))
print(type(bool1))
print(type(str1))
print(type(list1))
print(type(tuple1))
print(type(dic1))
# 可以用 type() 方法 来查看变量的类型