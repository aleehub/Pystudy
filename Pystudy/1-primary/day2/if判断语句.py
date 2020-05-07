# if 语句是用来判断的, 其使用的格式如下：

"""
if 要判断的条件：
    条件成立时，要做的事情

"""

# demo1

age1 = 30

if age1 >= 18:
    print("我已经满18岁了")


# demo2

age2 = 17

if age2 >= 18:
    print("我已经满18岁了")


# 只有if 中的条件被满足时, if下的语句才会被执行


# 练一练

myAge = int(input("输入你的年龄:"))

if myAge >= 18:
    print("哥，已成年，网吧可以去了！")
else:
    print("未成年，去写作业！")