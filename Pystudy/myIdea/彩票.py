import  random
import time
import  datetime

def doubleChromosphere():

    list = []  # 创建空列表
    i = 0
    while i < 6:
         a = random.randint(1,33)
         if a not in list:          # 判断表内是否已存在随机数，如果不存在则将随机数加入空表
             list.append(a)
             i += 1
         else:                      # 如果存在，则重新循环
             continue

    b = str(random.randint(1,16))   # 蓝球选号

    list.sort()                     # 将红球列表，排好序

    list.append(b)                  # 加入蓝球号码

    return list

def superLotto():

    list = []  # 创建空列表
    i = 0
    while i < 5:
         a = random.randint(1,35)   # 红球球选号
         if a not in list:          # 判断表内是否已存在随机数，如果不存在则将随机数加入空表
             list.append(a)
             i += 1
         else:                      # 如果存在，则重新循环
             continue

    list.sort()                     # 将红球列表，排好序

    j = 0
    while j < 2:
         b = str(random.randint(1,12))    # 蓝球选号
         if b not in list:          # 判断表内是否已存在随机数，如果不存在则将随机数加入空表
             list.append(b)
             j += 1
         else:                      # 如果存在，则重新循环
             continue

    return list

def duozhu(num,tag):

    allList=[]            # 创建多注列表
    if tag == 1:
        for i in range(num):
            allList.append(doubleChromosphere())

        for i in allList:
            for j in i:
                print(j,end=" ",flush=True)
                time.sleep(0.3)
            time.sleep(0.8)
            print("\n")

        return allList
    elif tag == 2:
        for i in range(num):
            allList.append(superLotto())

        for i in allList:
            for j in i:
                print(j, end=" ", flush=True)
                time.sleep(0.3)
            time.sleep(0.8)
            print("\n")

        return allList


while 1:
    tag = int(input("请选择玩法:\n 1.双色球\n 2.大乐透\n 3.退出\n"))

    if tag == 3:

        break

    elif tag !=1 and tag!=2:

        print("输入数字错误!\n请重新输入!")
        print("*"*30)

    else:
        num = int(input("注数："))

        value = duozhu(num,tag)

        f = open('记录.txt','a')

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("*"*30)
        f.write("\n")
        if tag == 1:
            f.write(f"{now}\n下注{num}次,选择双色球玩法,模拟彩票如下:\n")
        else:
            f.write(f"{now}\n下注{num}次,选择大乐透玩法,模拟彩票如下:\n")

        for i in value:
            f.write(str(i)+"\n")

        f.write("*" * 30)
        f.write("\n")
        f.close()



















