import os



foldName = 'F:\some video\亲爱的，热爱的'

dirList = os.listdir(foldName)


for name in dirList:
    print(name)

    index1 = name.rfind("第")
    index2 = name.rfind("集")
    index3 = name.rfind(".")
    if index1 == -1 or index2 == -1:
        print(name)
    else:
        newName = name[:index1] + "(" + name[index1 + 1:index2] + ")" + name[index3:]

        print(newName)

        os.rename(foldName + "/" + name, foldName + "/" + newName)

