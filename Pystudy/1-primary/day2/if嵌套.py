# 练一练


balance = 0
seat = 8

balance = float(input("输入你的余额："))

if balance > 2:

    print("你可以上公交车！")
    if seat > 0:
        print("你可以坐下！")

    else:
        print("你要站着！")
else:
    print("你的余额不足，不许上车！")