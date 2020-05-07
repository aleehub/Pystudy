# 双引号或者单引号中的数据

a = 'my name is lyh'
b = "my name is ycy"

print(a, b)

"""
字符串输出
    1.格式化操作符
    2.f-strings
        f-strings 提供一种简洁易读的方式，可以在字符串中包含Python表达式，
        f-strings 以字母'f'或'F'为前缀，格式化字符使用一对单引号，双引号，三单引号，三双引号，格式化字符串中      
"""

# demo1

name = '峰哥'
age = 33

format_string1 = f'我的名字是{name},我的年龄是{age}'

# demo2

format_string2 = f'3+5={3 + 5}'

print(format_string1)
print(format_string2)
