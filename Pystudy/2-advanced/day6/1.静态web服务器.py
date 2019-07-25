# 写出组装固定页面数据的响应报文




# 1.开发自己的静态web服务器


# 实现步骤:
#
#   1.编写一个TCP服务端程序
#   2.获取浏览器发送的http请求报文数据
#   3.读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器。
#   4.HTTP响应报文数据发送完成以后，关闭服务于客户端的套接字。


# 2. 静态web服务器-返回固定页面数据


import socket


# 构建main函数
if __name__ == '__main__':

    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)


    tcp_server_socket.bind(("",9090))


    tcp_server_socket.listen(128)

    while True:

        new_socket,ip_port = tcp_server_socket.accept()


        recv_client_data = new_socket.recv(4096)

        if len(recv_client_data) == 0:

            new_socket.close()

            print("浏览器下线了")

            continue

        recv_client_content = recv_client_data.decode("utf-8")

        print(recv_client_content)

        recv_list = recv_client_content.split(" ")

        file_path = recv_list[1]

        if file_path == "/":

            file_path = "/index.html"

        try :

            with open("static"+file_path,"rb") as file:

                file_data = file.read()

        except Exception:

            with open("static/error.html","rb") as file:

                file_data = file.read()

            response_line = "HTTP/1.1 500 NOT FOUND\r\n"

            response_header = "Server: PWS1.0\r\n"

            response_body = file_data

            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body

            new_socket.send(response_data)

            new_socket.close()

        else:

            response_line = "HTTP/1.1 200 OK\r\n"

            response_header = "Server: PWS1.0\r\n"

            response_body = file_data


            response_data = (response_line+response_header+"\r\n").encode("utf-8")+response_body

            new_socket.send(response_data)

            new_socket.close()




