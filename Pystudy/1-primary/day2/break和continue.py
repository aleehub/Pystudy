# break 在循环过程中 如果满足某条件就打断循环

name = "itheima"

for i in name:
    print("------")
    if i == "e":
        break

    print(i)

# 如果break没有执行，会接下来执行else语句
else:
    print("not break")

print("-------------------------")


# break 立即结束break所在的循环

# continue 打断满足条件的本次循环，不再执行条件后循环语句，执行下次循环

for i in name:
    print("------")
    if i == "e":
        continue

    print(i)

    # 如果整个循环没有执行，会接下来执行else语句
else:
    print("not break")

# 用来结束本次循环，开始执行下次循环

#  break/continue 只能在循环中使用
#  break/continue在循环嵌套中只对最近的 一层循环起作用