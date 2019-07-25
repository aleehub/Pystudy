import framework
import threading
import socket
import sys


# 定义静态web服务器类

class HttpWebSocket(object):

    def __init__(self, port):

        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        tcp_server_socket.bind(("", port))

        tcp_server_socket.listen(128)

        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket):

        recv_data = new_socket.recv(4096)

        if len(recv_data) == 0:
            print("浏览器下线了")
            new_socket.close()
            return

        recv_content = recv_data.decode("utf-8")

        request_list = recv_content.split(" ", maxsplit=2)

        request_path = request_list[1]

        if request_path == "/":
            request_path = "/index.html"

        if request_path.endswith(".html"):

            env = {
                "request_path": request_path
            }

            status, headers, response_body = framework.handle_request(env)

            response_line = "HTTP/1.1 %s\r\n" % status

            response_header = ""

            for header in headers:
                response_body += "%s:%s\r\n" % header

            response_data = (response_line +
                             response_header +
                             "\r\n" + response_body).encode("utf-8")

            new_socket.send(response_data)

            new_socket.close()


        else:

            try:

                with open("static" + request_path, "rb") as file:

                    file_data = file.read()

            except Exception as e:

                with open("static/error.html", "rb") as file:

                    file_data = file.read()

                response_line = "HTTP/1.1 400 NOT FOUND\r\n"

                response_header = "Server: PWS1.0\r\n"

                response_body = file_data

                response_data = (response_line + response_header + "\r\n").encode("utf8") + response_body

                new_socket.send(response_data)

            else:
                response_line = "HTTP/1.1 200 OK\r\n"

                response_header = "Server: PWS1.0\r\n"

                response_body = file_data

                response_data = (response_line + response_header + "\r\n").encode("utf8") + response_body

                new_socket.send(response_data)

            finally:

                new_socket.close()

    def start(self):

        new_socket, ip_port = self.tcp_server_socket.accept()

        sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))

        sub_thread.setDaemon(True)

        sub_thread.start()


def main():
    if len(sys.argv) != 2:
        print("please write python3 xxx.py 端口号")

        return

    if not sys.argv[1].isdigta:

        print("please write python3 xxx.py 端口号")

        return

    else:
        port = int(sys.argv[1])

        web_server = HttpWebSocket(port)

        web_server.start()
