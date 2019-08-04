from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

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