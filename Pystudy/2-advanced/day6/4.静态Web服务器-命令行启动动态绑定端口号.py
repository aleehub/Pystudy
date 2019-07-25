
import socket

import threading

import sys


# 创建web服务器类

class HttpWebServer(object):

    def __init__(self,port):

        #创建套接字

        tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # 设置端口号复用，程序退出端口立即释放

        tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

        # 绑定端口号

        tcp_server_socket.bind(("",port))

        # 设置监听

        tcp_server_socket.listen(128)

        print("first step")

        # 保存套接字

        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket):

        # 代码执行到此，说明连接建立成功
        recv_client_data = new_socket.recv(4096)

        print("third step")

        if len(recv_client_data) == 0:

            print("浏览器下线了！")

            new_socket.close()

            return


        # 对接收数据解码

        recv_client_content = recv_client_data.decode("utf-8")

        # 对请求内容设置列表

        request_list = recv_client_content.split(" ",maxsplit = 2)

        # 取出请求路径

        request_path = request_list[1]

        if request_path == "/":

            request_path = "/index.html"

        # 动态打开请求路径

        try:
            with open("static"+request_path,"rb") as file:

                # 读取网页数据
                file_data = file.read()

        except Exception as e:

            # 响应行
            response_line = "HTTP/1.1 404 NOT FOUND\r\n"

            # 响应头
            response_header = "Server: NBW/1.0\r\n"

            with open("static/error.html", "rb") as file:

                file_data = file.read()

            # 响应体
            response_body = file_data

            # 组合发送数据
            send_data = (response_line+response_header+"\r\n").encode("utf-8")+response_body

            new_socket.send(send_data)

        else:

            response_line = "HTTP/1.1 202 OK\r\n"

            # 响应头
            response_header = "Server: NBW/1.0\r\n"

            # 响应体
            response_body = file_data

            # 组合发送数据
            send_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body

            new_socket.send(send_data)

        finally:

            # 关闭客户端套接字
            new_socket.close()

    # 设置启动方法

    def start(self):

        # 服务端套接字等待连接
        while True:

            new_socket,ip_port = self.tcp_server_socket.accept()

            # 设置子线程
            print("second step")

            sub_thread = threading.Thread(target=self.handle_client_request,args=(new_socket,))

            # 设置守护进程
            sub_thread.setDaemon(True)

            # 启动子线程

            sub_thread.start()



# 程序入口函数

def main():

    print(sys.argv)

    if len(sys.argv) != 2:
        print("执行命令如下: python3 xxx.py 8000")

        return

    # 判断字符串是否都是又数字组成

    if not sys.argv[1].isdigit():

        print("执行命令如下: python3 xxx.py 8000")

        return

    # 获取终端命令行参数

    port = int(sys.argv[1])

    # 实例化对象
    web_server = HttpWebServer(port)

    # 启动服务器
    web_server.start()







if __name__ == '__main__':


    main()

