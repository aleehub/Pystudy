# 多任务 TCP服务程序开发

# 1. 目前我们开发的TCP服务端程序只能服务于一个客户端，如何开发一个多任务版的TCP服务端程序能够服务于多个客户端呢?
#
# 完成多任务，可以使用线程，比进程更加节省内存资源

# 2. 具体实现步骤
#   1.编写一个TCP服务端程序，循环等待接受客户端的连接请求
#   2.当客户端和服务端建立连接成功，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞
#   3.把创建的子线程设置成为守护主线程，防止主线程无法退出。


# demo:

import socket

import threading

# 处理客户端的请求操作
def handle_client_request(service_client_socket,ip_port):

    """循环接收客户端发送的数据"""

    while True:
        # 接收客户端发送的数据

        recv_data = service_client_socket.recv(1024)

        # 容器类型判断是否有数据可以直接使用if语句进行判断，如果容器类型里面有数据表示条件成立，否则条件失败
        # 容器类型: 列表、字典、元组、字符串、set、range、二进制数据

        if recv_data:
            print(recv_data.decode("utf-8"),ip_port)

            service_client_socket.send("ok,问题正在处理中...".encode("utf-8"))

        else:
            print("客户端下线了")

            break

    # 终止和客户端的通信

    service_client_socket.close()


if __name__ == '__main__':

    """ 创建tcp服务端套接字"""

    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 设置端口复用

    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    # 绑定端口号

    tcp_server_socket.bind(("",9090))

    # 设置监听

    tcp_server_socket.listen(128)

    # 循环等待连接
    while True:

        # 等待接收客户端的连接请求
        service_client_socket,ip_port = tcp_server_socket.accept()
        print("客户端连接成功了，",ip_port)
        # 当客户端和服务端建立连接成功以后，需要创建一个子线程，不同子线程负责接收不同客户端的信息
        client_thread = threading.Thread(target = handle_client_request,args=(service_client_socket,ip_port) )

        # 设置守护主进程
        client_thread.setDaemon(True)

        # 启动子线程
        client_thread.start()




# 小结

# 1. 编写一个TCP服务端程序，循环等待接收客户端的连接请求

# 2. 当客户端和服务端建立连接成功后，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞

# 3. 把创建的子线程设置为守护主线程，防止主线程无法退出

