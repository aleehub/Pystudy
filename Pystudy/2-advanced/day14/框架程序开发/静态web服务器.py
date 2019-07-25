import socket
import threading
import sys
from 框架程序开发 import framwork


class HttpWebServer(object):

    def __init__(self, port):

        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用，程序退出端口立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    # 处理客户请求
    @staticmethod
    def handle_client_request(new_socket):

        # 代码执行到此，说明链接建立成功，开始接收请求数据
        recv_client_data = new_socket.recv(4096)
        # 如果接收数据长度为0，则代表浏览器关闭
        if len(recv_client_data) == 0:
            print("浏览器关闭了!")
            # 关闭套接字
            new_socket.close()
            # 退出函数
            return

        # 对接收数据进行二进制解码
        recv_client_content = recv_client_data.decode("utf-8")

        # 分割解码数据，生成一个列表
        request_list = recv_client_content.split(" ", maxsplit=2)
        # 从列表中提取请求路径
        request_path = request_list[1]

        print(request_path)

        # 判断请求路径是否是根目录，如果成立，则指定首页返回
        if request_path == "/":
            request_path = "/index.html"

        # 根据请求文件是否为html后缀，来判断是否为动态资源
        if request_path.endswith(".html"):

            env = {
                "request_path": request_path
            }

            # 获取处理结果
            status, headers, response_body = framwork.handle_request(env)

            # 使用框架处理的数据拼接报文
            # 响应行
            response_line = "HTTP/1.1 %s\r\n" % status
            # 响应头
            response_header = ""
            for header in headers:
                # 拼接多个响应头
                response_header += "%s: %s\r\n" % header

            response_data = (response_line +
                             response_header +
                             "\r\n" +
                             response_body).encode("utf-8")

            # 发送数据
            new_socket.send(response_data)
            # 关闭socket
            new_socket.close()


        else:
            """静态资源请求"""
            try:
                # 动态打开指定文件
                with open("static" + request_path, "rb") as file:
                    # 读取文件数据
                    file_data = file.read()
            except Exception as e:
                # 请求资源不存在
                # 响应行
                response_line = "HTTP/1.1 404 NOT FOUND\r\n"
                # 响应头
                response_header = "Sever: PWS1.0\r\n"
                with open("static/error.html", "rb") as file:
                    file_data = file.read()
                # 响应体
                response_body = file_data
                # 拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode("utf-8")
                #  发送数据
                new_socket.send(response_data)

            else:
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 响应头
                response_header = "Server: PWS1.0"
                # 响应体
                response_body = file_data
                # 拼接数据
                response_data = (response_line + response_header + "\r\n").encode("utf-8")
                # 发送数据
                new_socket.send(response_data)

    def start(self):

        while True:
            # 等待接收客户端的连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置守护主进程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()


def main():
    # 获取命令行参数
    if len(sys.argv) != 2:
        print("执行命令如下：python3 xxx.py 9000")
        return
    # 判断端口号是否为数字
    if not sys.argv[1].isdigit():
        print("执行命令如下：python3 xxx.py 9000")
        return
    port = int(sys.argv[1])
    web_server = HttpWebServer(port)
    web_server.start()


if __name__ == '__main__':
    main()
