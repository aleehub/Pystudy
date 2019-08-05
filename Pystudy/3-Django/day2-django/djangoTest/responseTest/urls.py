from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^demo_view/$',views.demo_view),
    url(r'^demo_quickstatus/$',views.demo_quickstatus),
    url(r'^demo_json/$',views.demo_json),
    url(r'^demo_redict/$',views.demo_redict),

]