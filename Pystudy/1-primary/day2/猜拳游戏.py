import random

player = int(input ('请输入：剪刀（0） 石头（1） 布（2）：'))


computer = random.randint(0,2)


if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):

    print("你赢了！")

elif player==computer:

    print('你们是平手！')

else :

    print("你输了！")

"""
在Python中使用随机数，要用random包
导入random包 import random

random.randint()

"""

