import os

funflag = 1

foldName = ''

dirList = os.listdir(foldName)


for name in dirList:
    print(name)

    index1 = name.rfind("第")
    index2 = name.rfind("集")
    index3 = name.rfind(".")
    if funflag == 1:

        newName = name[:index1]+"("+name[index1+1:index2]+")"+name[index3:]



    elif funflag == 2:

        num = len("[东哥出品]-")
        newName = name[num:]

    print(newName)


    os.rename(foldName+"/"+name,foldName+"/"+newName)


