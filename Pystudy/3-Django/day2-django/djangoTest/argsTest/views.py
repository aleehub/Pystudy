import json

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
from django.utils import jslex


def index(request):

    return HttpResponse("hello the world!")


def say(request):

    url = reverse('argsTest:say')

    print(url)

    return HttpResponse('say')

# 1. URL路径参数
#   在定义路由URL是，可以使用正则表达式提取参数的方法从URL中获取请求参数，Django会将提取到的参数直接传递到实体的传入参数中。

# url(r'^weather/([a-z]+)/(\d{4})/$',views.weather1),
# 未命名参数按定义顺序传递

def weather1(request,city,year):

    print(f"{city}")

    print(f"{year}")

    return HttpResponse("天气1")

# url(r'^weather/(?p<city>[a-z]+)/(?p<year>\d{4})/$',views.weather2)
# 命名参数按名字传递

def weather2(request,year,city):

    print(f"{city}")

    print(f"{year}")

    return HttpResponse("天气2")
# 1.get提交路径参数
# Django中的QueryDict对象
# 定义在django.http.QueryDict
# HttpRequest对象的属性 GET/POST都是QueryDict类型的对象
# 与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
def test1(request):

    # 用postman测试，输入一个路径参数，
    # localhost:8000/argsTest/?key1=1
    # request对象的GET属性为django下的查询字典对象
    # 值都为一个列表

    print(request.GET,type(request.GET))

    # < QueryDict: {'key1': ['2'], 'key2': ['3', '4', '5']} >
    # <class 'django.http.request.QueryDict'>

    dic1= request.GET.get("key1")

    # 当传递参数存在多个值时，用get获取参数值，只会获取到最后一个值
    dic2 =request.GET.get("key2")
    # 而当用getlist时则可以获取多个值
    dic2 =request.GET.getlist("key2")

    print(dic1)

    print(dic2)

    return HttpResponse("test1")


# 2.post请求体表单提交方式
# 当采用表单提交方式时。django框架自动提供了一个csrf防护，用来阻止第三方的非法提交
# 这需要获取一个csrf秘钥，才能成功提交，否则会被拦截
# 如果使用第三方的测试工具测试时，则需要到主程序设置页面，将中间件的csrf中间件给注释掉
# 'django.middleware.csrf.CsrfViewMiddleware',

def test2(request):

    requestData = request.POST

    a =requestData.get("key1")

    b =requestData.getlist("key2")

    print(a,b)

    return HttpResponse("test2")

# 3.post请求体提交非表单类型
# 非表单类型的请求体数据。django无法自动解析，可以通过 request.body属性获取最原始的请求体数据，自己按照请求体格式 (Json,xml)进行解析
# request.body返回bytes类型

def test3(request):

    # body属性获取的是二进制数据
    request_byte = request.body

    # 将二进制数据解码成字符串
    request_str = request_byte.decode()

    # 将解码来的json数据，用json中的loads函数生成一个python字典

    # pycharm 快捷键 alt+enter导入相关包
    # 生成一个python字典
    req_data = json.loads(request_str)

    print(req_data)

    return HttpResponse("test3")

# 4.请求头
# 可以通过request.META属性获取请求头headers中的数据
# request.META为字典类型

# 常见的请求头如：
#
# CONTENT_LENGTH – The length of the request body (as a string).
# CONTENT_TYPE – The MIME type of the request body.
# HTTP_ACCEPT – Acceptable content types for the response.
# HTTP_ACCEPT_ENCODING – Acceptable encodings for the response.
# HTTP_ACCEPT_LANGUAGE – Acceptable languages for the response.
# HTTP_HOST – The HTTP Host header sent by the client.
# HTTP_REFERER – The referring page, if any.
# HTTP_USER_AGENT – The client’s user-agent string.
# QUERY_STRING – The query string, as a single (unparsed) string.
# REMOTE_ADDR – The IP address of the client.
# REMOTE_HOST – The hostname of the client.
# REMOTE_USER – The user authenticated by the Web server, if any.
# REQUEST_METHOD – A string such as "GET" or "POST".
# SERVER_NAME – The hostname of the server.
# SERVER_PORT – The port of the server (as a string).

def get_headers(request):

    print(request.path)
    print(request.META)
    for i ,j in request.META.items():

        print(i,":",j)

    print(request.META['CONTENT_TYPE'])
    return HttpResponse('OK')



# 6 其他常用HttpRequest对象属性
# method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
# user：请求的用户对象。
# path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
# encoding：一个字符串，表示提交的数据的编码方式。
# 如果为None则表示使用浏览器的默认设置，一般为utf-8。
# 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值。
# FILES：一个类似于字典的对象，包含所有的上传文件。