# 1.家具分为不同的类型，并占用不同的面积

# 2. 输出家具信息时，显示家具的类型和家具占用的面积

# 3.  房子有自己的地址和占用的面积

# 4. 房子可以添加家具，如果房子的剩余面积可以容纳家具，则提示家具添加成功，否则提示添加失败

# 5. 输除房子信息时，可以显示房子的地址、占地面积、剩余面积



class Home(object):

    def __init__(self,area):

        self.area = area

        self.containsItem = []


    def __str__(self):

        msg = "当前房间可用面积为："+str(self.area)

        if len(self.containsItem) > 0:

            msg = msg + ",容纳的物品有："

            for temp in self.containsItem:

                msg = msg + temp.getName() + ","

            msg = msg.strip(",")

        return msg



    def accommodateItem(self,item):

        needArea = item.getUserArea()

        if self.area > needArea:

            self.containsItem.append(item)

            self.area -= needArea

            print("ok:已经存放在房间中")

        else:
            print(f"err:房间可用面积为：{self.area},但是当前要存放的物品需要的面积为{needArea}")


class Bed(object):


     def __init__(self,area,name = "床"):

            self.name = name

            self.area = area


     def __str__(self):

            msg = "床的面具为" + str(self.area)

            return msg

     def getUserArea(self):

         return self.area


     def getName(self):

         return self.name



newHome = Home(100)

print(newHome)

newBed1 = Bed(20)

print(newBed1)

newHome.accommodateItem(newBed1)

print(newHome)

newBed2 = Bed(12,"席梦思")

print(newBed2)

newHome.accommodateItem(newBed2)

print(newHome)


# 如果一个对象与另外一个对象有一定的关系，那么一个对象可用是另一个对象的属性




