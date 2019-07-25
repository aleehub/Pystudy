# 多线程版的多任务web服务器程序

# demo

import socket

import threading


# 处理客户端的请求

def  handle_client_request(new_socket):

    # 代码执行到此，说明连接建立成功

    recv_client_data = new_socket.recv(1024)

    if len(recv_client_data) == 0:

        print("浏览器关闭了")

        new_socket.close()

        return

    # 对二进制数据进行解码
    recv_client_content = recv_client_data.decode("utf-8")
    print(recv_client_content)

    # 根据指定字符串进行分割，最大分割次数指定为2

    request_list = recv_client_content.split(" ",maxsplit = 2)

    # 获取请求资源路径

    request_path = request_list[1]
    print(request_path)

    # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
    if request_path == "/":

        request_path = "/index.html"

    try:
        # 动态打开指定文件
        with open("static"+request_path,"rb") as file:

            # 读取文件数据
            file_data = file.read()

    except Exception as e:

        # 请求资源不存在，返回404数据
        # 响应行
        response_line = "HTTP/1.1 404 NOT FOUND\r\n "
        # 响应头
        response_header = "Server: PW1.0\r\n"

        with open("static/error.html","rb") as file:

            file_data = file.read()

        response_body = file_data

        send_data = (response_line+response_header+"\r\n").encode("utf-8")+response_body


        new_socket.send(send_data)

    else:

        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n "
        # 响应头
        response_header = "Server: PW1.0\r\n"

        with open("static"+request_path, "rb") as file:

            file_data = file.read()

        response_body = file_data

        send_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body

        new_socket.send(send_data)

    finally:

        # 关闭服务与客户端的套接字

        new_socket.close()

# 程序入口函数

def main():

    # 创建tcp服务端套接字

    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 设置端口复用,程序退出端口立即释放

    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    # 绑定端口号

    tcp_server_socket.bind(("",9090))

    # 设置监听

    tcp_server_socket.listen(128)

    # 循环重复接收客户端请求

    while True:

        # 等待接收客户端的连接
        new_socket,ip_port = tcp_server_socket.accept()

        # 打印新建立连接

        print("浏览器连接了:",ip_port)

        # 当客户端建立连接，建立子线程

        sub_thread = threading.Thread(target=handle_client_request,args=(new_socket,))

        # 守护主线程

        sub_thread.setDaemon(True)

        # 启动子线程执行对应的任务

        sub_thread.start()


if __name__ == '__main__':

    main()






