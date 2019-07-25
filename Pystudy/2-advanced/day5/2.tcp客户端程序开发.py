# 1.开发TCP客户端程序开发步骤回顾

# 创建客户端套接字对象
# 和服务端套接字建立连接
# 发送数据
# 接收数据
# 关闭客户端套接字


# 2. socket 类的介绍
# 导入 socket 模块 import socket
#
# 创建客户端 socket 对象 socket.socket(AddressFamily, Type)
#
# 参数说明:
#
# AddressFamily 表示IP地址类型, 分为TPv4和IPv6
# Type 表示传输协议类型

# 方法说明:
#
# connect((host, port)) 表示和服务端套接字建立连接, host是服务器ip地址，port是应用程序的端口号
# send(data) 表示发送数据，data是二进制数据
# recv(buffersize) 表示接收数据, buffersize是每次接收数据的长度


# demo


import socket

if __name__ == '__main__':

        """创建客户端套接字对象"""
        # 1.AF_INET: 表示ipv4
        # 2.SOCK_STREAM: tcp传输协议
        tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


        # 和服务端套接字建立连接
        tcp_client_socket.connect(("192.168.253.138",8080))


        # 发送数据
        send_data = "hello server,i am cliet ycy".encode("gbk")

        print(send_data)

        tcp_client_socket.send(send_data)

        # 接收数据

        recv_data = tcp_client_socket.recv(1024)

        recv_content=recv_data.decode("utf-8")

        print(recv_content)

        # 关闭客户端套接字
        tcp_client_socket.close()

# 说明：

#       1.str.encode(编码格式) 表示吧字符串编码成为二进制
#       2.data.decode(编码格式) 表示吧二进制解码成为字符串


# 小结：
# 1. 导入socket模块
# 2. 创建TCP套接字"socket"
#      参数1：socket.AF_INET , 表示IPV4 地址
#      参数2：SOCK_STREAM ,表示TCP传输协议类型
# 3.发送数据"send"
#      参数1：要发送的二进制数据
#4. 接收数据"recv"
#       参数1：表示每次接收数据的大小，单位是字节
#5.关闭套接字"socket"表示通信完成

