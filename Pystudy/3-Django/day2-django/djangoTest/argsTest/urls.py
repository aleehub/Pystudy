from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^index/',views.index,name='index'),

    url(r'^say/',views.say,name='say'),

    url(r'^weather1/([a-z]+)/(\d{4})/$',views.weather1),

    # url(r'^weather2/(?p<city>[a-z]+)/(?p<year>\d{4})/$',views.weather2),

    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),

]