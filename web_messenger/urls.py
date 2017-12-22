from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    url(r'^loginvalidation',views.validation,name='validation'),
    url(r'^registration',views.registration,name='registration'),
    url(r'^register',views.register,name='register'),
    url(r'^test',views.test,name='test'),
]