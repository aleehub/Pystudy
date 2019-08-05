from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^demo_cookie/$',views.demo_cookie),
    url(r'^demo_readCookie/$',views.demo_readCookie),


]