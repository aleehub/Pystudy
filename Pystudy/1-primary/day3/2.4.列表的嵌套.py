# 列表中可以嵌套另一个列表

# 列表中的元素可以是不同的数据类型

# 应用
# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

import random

offices = [[], [], []]

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

i = 0

for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

i = 1

for temNames in offices:
    print(f"办公室{i}的人数是{len(temNames)}")

    i += 1
    for name in temNames:
        print(name, end=" ")
    print()
    print("-" * 20)
