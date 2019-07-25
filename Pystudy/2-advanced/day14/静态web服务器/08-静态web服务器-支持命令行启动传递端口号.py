# 1.等待客户端链接，有一个新的客户端链接，创建一个新的线程服务器客户端
# 2.设置子线程为守护主线程，防止主线程不能直接退出



import socket
import threading
import sys


class HttpWebServer(object):

    def __init__(self, port):
        # 1.实现tcp服务器
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        tcp_server_socket.bind(("", port))

        tcp_server_socket.listen(128)

        # 设置实例属性，
        self.tcp_server_socket = tcp_server_socket


    def start(self):
        while True:
            # 等待客户端链接
            new_service_client_socket, client_address_info = self.tcp_server_socket.accept()
            print("浏览器访问： ", client_address_info)

            # 一旦有新的客户端链接，创建一个新的线程服务客户端
            sub_thread = threading.Thread(target=self.handler_client, args=(new_service_client_socket,))
            # 为了防止主线程无法直接退出，设置所有子线程为守护主线程。 主线程结束，所有子线程的通讯也结束
            sub_thread.setDaemon(True)
            # 启动线程
            sub_thread.start()

    # 设置静态方法：参数不需要接收self
    # 实例方法: self
    # 静态方法: 单例模式
    # 类方法: cls
    @staticmethod
    def handler_client(new_service_client_socket):
        # 2.接收浏览器发送的请求报文
        request_data = new_service_client_socket.recv(4096)
        if len(request_data) == 0:
            print("浏览器关闭了")
            new_service_client_socket.close()
            return

        # 解码接收到的请求报文
        request_content = request_data.decode("utf-8")
        print("接收到请求报文： ", request_content)
        # 把请求报文按照空格分割
        # maxsplit: 分割两次
        request_list = request_content.split(" ", maxsplit=2)

        print(request_list)

        # 取出请求资源路径
        file_path = request_list[1]

        # 设置默认首页
        if file_path == "/":
            file_path = "/index.html"

        try:
            # 3.打开指定页面文件，并且拼接成响应报文返回给浏览器
            with open("static" + file_path, "rb") as file:
                file_data = file.read()

        except Exception as e:
            # 返回404页面
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_head = "Server: NBS/1.1\r\n"
            # 空行

            # 打开404的错误页面文件
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            # 响应体
            response_body = file_data

            # 拼接成响应报文
            response_data = (response_line + response_head + "\r\n").encode("utf-8") + file_data

            # 把响应报文发送给浏览器
            new_service_client_socket.send(response_data)

        else:
            # 返回指定页面
            # 拼接成响应报文

            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_head = "Server: NBS/1.1\r\n"
            # 空行

            # 响应体
            response_body = file_data

            # 拼接成响应报文
            response_data = (response_line + response_head + "\r\n").encode("utf-8") + file_data

            # 把响应报文发送给浏览器
            new_service_client_socket.send(response_data)

        # 4.关闭socket
        new_service_client_socket.close()


def main():
    # ['xxx.py', '9090']
    print(sys.argv)
    # 参数个数错误
    if len(sys.argv) != 2:
        print("用法错误： python3 web.py 端口号")
        return

    # 参数类型错误
    if not sys.argv[1].isdigit():
        print("用法错误： python3 web.py 端口号(端口号必须是数字)" )
        return

    # 转换字符串为整数
    port = int(sys.argv[1])

    web = HttpWebServer(port)
    web.start()


if __name__ == '__main__':
    main()
