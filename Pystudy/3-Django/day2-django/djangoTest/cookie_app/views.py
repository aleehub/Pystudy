from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


#cookie_app

# cookie_app ,有时也用器复数形式cookies,值某些网站为了辨别用户身份，进行session跟踪而存储在用户本地终端的数据

# Cookie最早是网景公司的前雇员Lou Montulli在1993年3月的发明。Cookie是由服务器端生成，发送给User-Agent（一般是浏览器），浏览器会将Cookie的key/value保存到某个目录下的文本文件内，下次请求同一网站时就发送该Cookie给服务器（前提是浏览器设置为启用cookie）。Cookie名称和值可以由服务器端开发自己定义，这样服务器可以知道该用户是否是合法用户以及是否需要重新登录等。服务器可以利用Cookies包含信息的任意性来筛选并经常性维护这些信息，以判断在HTTP传输中的状态。Cookies最典型记住用户名。

# cookie的特点
#   cookie以键值对key-value 形势进行信息的存储
#   cookie基于域名安全，不同域名的cookie是不能访问的

#  设置cookie
# 通过HttpResponse对象照片那个的set_cookie方法来设置cookie


def demo_cookie(request):

    response = HttpResponse("这是一个cookie测试！")

    # HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)
    response.set_cookie("name",value="yangchaoyue")
    response.set_cookie("age",value="21")

    return response

# 读取cookie

# 可以通过HttpRequest对象的cookie属性来读取本次请求携带的cookie值。request.COOKIES为字典类型

def demo_readCookie(request):

    print(request.COOKIES)
    # {'name': 'yangchaoyue', 'age': '21'}
    return HttpResponse(f"得到的cookies数据是 {request.COOKIES}")