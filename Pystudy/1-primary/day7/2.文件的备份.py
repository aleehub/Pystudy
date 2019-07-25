# 制作文件的备份
# 输入文件的名字，然后程序自动对文件进行备份


oldFileName = input("请输入旧文件的名字：")

index = oldFileName.rfind(".")

newFileName = oldFileName[:index]+"[备份]"+oldFileName[index:]


f = open(oldFileName)

content = f.readlines()

f.close()

f = open(newFileName,"w")

for i in content:
    f.write(i)

f.close()