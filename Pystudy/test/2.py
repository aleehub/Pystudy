# mysql  -uroot -pmysql

# create database heima charset=utf8 ;
# use heima;
# create table students(
#  id int unsigned primary key auto_increment not null,
#  name varchar(20) not null,
#  passwd varchar(20) not  null
# );


import pymysql

class Start(object):

    def __init__(self):

        self.name = ""
        self.passwd = ""



    def register(self):

        print("欢迎来到注册页面:")

        def getname():

            name = input("请输入用户名:")
            if len(name) == 0 or len(name)>10:
                print("用户名格式错误,请输入10位以内不为空的字符")
                getname()
            else :
                return name

        def getpasswd():

            passwd1 = input("请输入密码:")

            if len(passwd1) == 0:

                print("密码格式错误,请输入10位以内不为空的字符")

                getpasswd()

            else:

                passwd2 = input("请确认密码:")

                if passwd1 != passwd2:

                    print("两次密码不一致，请重新输入！")

                    getpasswd()

                else:

                    return passwd1

        self.name = getname()

        self.passwd = getpasswd()

        # 创建连接对象
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='mysql',
                               database='heima',
                               charset='utf8')

        cursor = conn.cursor()

        sql1 = "select * from user where name = '%s';"%self.name

        row_count = cursor.execute(sql1)

        if row_count != 0:
            print("该用户名已存在, 请重新注册!")

            cursor.close()
            conn.close()
            self.register()
        else:
            sql2 = "insert into user(name,passwd) values('%s','%s');"%(self.name,self.passwd)

            row_count = cursor.execute(sql2)

            conn.commit()
            cursor.close()
            conn.close()
            print("注册成功")

            self.index()

    def login(self):

        print("欢迎来到登录页面:")

        def getname():

            name = input("请输入用户名:")

            if len(name) == 0 or len(name)>10:
                print("用户名格式错误,请输入10位以内不为空的字符")

                getname()

            else :
                return name

        def getpasswd():

            passwd = input("请输入密码:")

            if len(passwd) == 0:
                print("密码格式错误,请输入10位以内不为空的字符")

                getpasswd()

            else:
                return passwd

        self.name = getname()

        self.passwd = getpasswd()

        # 创建连接对象
        conn = pymysql.connect(host='localhost',
                               port=3306, user='root',
                               password='mysql',
                               database='heima',
                               charset='utf8')

        cursor = conn.cursor()

        sql = "select * from user where name ='%s' and passwd = '%s';"%(self.name,self.passwd)

        row_count = cursor.execute(sql)
        if row_count == 0:
            print("用户名或密码错误, 请重新输入!")

            cursor.close()
            conn.close()
            self.login()
        else:
            conn.commit()
            cursor.close()
            conn.close()
            print("登录成功")
            self.index()

    def index(self):

        self.name = ''
        self.passwd = ''
        print("-------欢迎来到黑马程序员---------")
        print("1:  注册")
        print("2:  登录")
        request = int(input("请输入功能对应的序号:"))

        if request == 1:
            self.register()
        elif request == 2:
            self.login()
        else:
            print("输入错误请重新输入")
            self.index()



def main():

    test = Start()
    test.index()


if __name__ == '__main__':

    main()



