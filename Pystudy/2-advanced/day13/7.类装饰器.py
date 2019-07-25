class Check(object):
    def __init__(self,func):

        # 初始化操作在此完成
        self._fn = func



    def __call__(self, *args, **kwargs):

        # 添加装饰函数

        print("请先登录")

        self._fn()






@Check
def comment():

    print("发表评论")



comment()


