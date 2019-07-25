# 获取首页数据
def index():
    # 响应状态
    status = "200 OK"
    # 响应头
    reponse_header = [("Server", "PWS2.0")]

    # 打开模板文件，读取数据

    with open("template/index.html", "r") as file:
        file_data = file.read()
