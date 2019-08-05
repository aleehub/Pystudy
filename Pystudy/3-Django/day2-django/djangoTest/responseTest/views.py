from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotModified, \
    HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseGone, \
    HttpResponseServerError, JsonResponse


# Create your views here.

# 响应

# 识图在接收请求并处理后，必须返回HttpResponse对象或子对象，Http

# HttpResponse(content=响应体,content_type=响应体数据类型,status=状态码)

def demo_view(request):

    # return HttpResponse('itcast python',status=400)

    #  其他写法

    # 响应体
    response = HttpResponse('itcast python')

    # 响应状态
    response.status_code =200

    # 响应头属性值
    response["itcast"] = 'python'

    return response


# HttpResponse 子类
# 不常用

# Django提供了一系列HttpResponse的子类。可以快速设置状态码

# HttpResponseRedirect 301
# HttpResponsePermanentRedirect 302
# HttpResponseNotModified 304
# HttpResponseBadRequest 400
# HttpResponseNotFound 404
# HttpResponseForbidden 403
# HttpResponseNotAllowed 405
# HttpResponseGone 410
# HttpResponseServerError 500

def demo_quickstatus(request):

    # 自动跳转到参数变量路径下，如果没有设置绝对路径则在当前路径下后添加参数字符为新路径
    # ./ 当前目录下
    # ../返回上一层目录
    response1 = HttpResponseRedirect("../demo_view")
    # response2 = HttpResponsePermanentRedirect("302")
    # response3 = HttpResponseNotModified()
    # response4 = HttpResponseBadRequest("400")
    # response5 = HttpResponseNotFound()
    # response6 = HttpResponseForbidden("403")
    # response7 = HttpResponseNotAllowed("405")
    # response8 = HttpResponseGone("410")
    # response9 = HttpResponseServerError("500")

    return response1


# 若要返回json对象
# 使用JsonResponse来构造对象


def demo_json(request):

    req_data ={
        'city':"beijing",
        'subject':'python'
    }
    # json字符串自动转为双引号字典类型。键值均为字符串
    return JsonResponse(req_data)


def  demo_redict(request):

    print(request)

    return redirect("../index.html")