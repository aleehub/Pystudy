# while  里面 嵌套while

# 通过while 来打印三角形

# 1
i = 0
while i < 5:
    j = 0
    while j <=5:
        print("*",end = " ")
        j += 1
    print()
    i += 1

#2
i = 1
while i <=5:
    j=1
    while j <= i:
        print("*",end=" ")
        j += 1
    print()
    i += 1

#3

import random
while 1:


    player = int(input('请输入：剪刀（0） 石头（1） 布（2）：'))

    computer = random.randint(0, 2)

    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):

        print("你赢了！")

    elif player == computer:

        print('你们是平手！')

    else:

        print("你输了！")