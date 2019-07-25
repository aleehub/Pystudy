class Student:
    """
    定义一个学生类,用来封装学生的4个信息
    """

    def __init__(self, id, name, score):
        """
        给对象添加3个属性
        :param id: 学号
        :param name: 姓名
        :param score: 分数
        """
        self.id = id
        self.name = name
        self.score = score

    def __str__(self):
        return "%s,%s,%s" % (self.id, self.name, self.score)