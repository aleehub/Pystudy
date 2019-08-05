
from django.shortcuts import render

# Create your views here.

# session 在计算机中，尤其在网络应用中，成为会话控制。Session对象存储特定用户会话所需的属性及配置信息。这样，当用户在应用程序的web页之间跳转，存储在session对象中的变量将不会丢失，而是在整个用户会话中一直存在下去，当用户请求来自 应用程序的web页时，如果该用户还没有会话，则Web服务器将自动创建一个Session对象，当会话过期或被放弃后。服务器将终止该对话 。Session对象最常见的一个用法就是存储用户的首选项。


# Session的作用

# session的作用就是它在web服务器上保持用户的状态信息供在任何时间从任何设备的页面 进行访问。
# 因为浏览器不需要存储任何郑重信息，所以 可以使用任何浏览器，及时是想pad或手机这样的浏览器设备。

# Session的特点

# 1. 依赖 cookies
# 2. 存储敏感。重要的信息
# 3. 支持更多字节
# 4. session共享问题

# 启用Session
# django项目默认启用session
# session中间件
# 'django.contrib.sessions.middleware.SessionMiddleware',

# Session操作

# 通过HttpRequest对象的session属性进行会话的读写操作。
# 1)以键值对的格式写session
# request["key"] = "value"

# 2)根据键读取值
# request.session.get("key",default)

# 3)清除所有session，在存储中删除值部分
# request.session.clear()

# 4)清除session数据，在存储中删除session的整条数据
# request.session.flush()

# 5)删除session中的指定键及值，在存储中只删除某个键及对应的值。
#del request.session['key']


# 6)设置session的有效期
# request.session.set_expiry(value)
# 如果value是一个整数，session将在value秒没有活动后过期。
# 如果value为0，那么用户session的cookie将在用户的浏览器关闭时过期
# 如果value为NONE，那么session有效期将采用系统默认值，默认为两周，可以通过在settting.py中设置SESSION_COOKIE_AGE来设置全局默认值





def demo_session(request):

    request.session["userID"] ="1234"
