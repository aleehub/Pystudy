from redis import *



if __name__ == '__main__':

    try:
        # 创建 StrictRedis对象，与redis服务器建立连接
        sr = StrictRedis(host="localhost",port=6379,db=0)

        # 添加键name,值为itheima
        # result1 = sr.set("name","yangchaoyue")

        # 

        #输出响应结果，如果添加成功则返回True，否则返回False
        print(result1)

        # 输出键的值，如果间不存在则返回None
        result2 = sr.get("name").decode()

        print(result2)

    except Exception as e:

        print(e)

    else:
        print("create success")
#

# from redis import *
#
# if __name__ == '__main__':
#
#     try:
#
#         #创建StrictRedis对象，与redis服务器建立连接
#
#         sr = StrictRedis()
#
#         #删除键name的值，如果键存在则删除，如果不存在则不操作
#
#         result = sr.delete("nae")
#
#         # 输出响应结果，如果删除成功则返回受影响的键鼠，否则则返回0
#         print(result)
#
#     except Exception as e:
#
#         print(e)


# 获取键

# from redis import *
#
# if __name__ == '__main__':
#
#     try:
#         # 创建StricRedis对象，与redis服务器建立连接
#
#         sr = StrictRedis()
#
#         # 获取所有的键
#
#         result = sr.keys()
#
#         for i in result:
#
#             i.decode()  # 没有返回值，不会对i进行改变。
#
#             print(i.decode())
#
#         # 输出响应结果
#
#         print(result)
#
#     except Exception as e:
#
#         print(e)





