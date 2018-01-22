from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    url(r'^loginvalidation',views.validation,name='validation'),
    url(r'^register',views.register,name='register'),
    url(r'^test',views.test,name='test'),
    url(r'^sendmessage',views.sendmessage,name='sendmessgae'),
    url(r'^autorefresh',views.autorefresh,name='autorefresh'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^deletesingle',views.deletesingle,name='deletesingle'),
    url(r'^delete',views.delete,name='delete'),
    url(r'^updateprofile',views.updateprofile,name='updateprofile')



]