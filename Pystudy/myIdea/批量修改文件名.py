import os

foldName = 'F:\Download'

dirList = os.listdir(foldName)


for name in dirList:
    print(name)

    index2 = name.rfind("g")
    if index2 == -1:
        print(name)
    else:
        newName = "将" + name[index2 + 1:]

        print(newName)

        os.rename(foldName + "/" + name, foldName + "/" + newName)

