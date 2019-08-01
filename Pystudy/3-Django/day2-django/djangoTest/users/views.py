from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    """
    index 视图
    :param request: 包含请求信息的请求对象
    :return:响应对象
    """

    return HttpResponse("HELLO WORLD!")