from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):

    return render(request,'login.html')

def validation(request):
    unm1=request.POST['user']
    pass1=request.POST['pwd']
    r=requests.get('http://localhost/messenger/3.php',params={'type':'login','un':unm1,'pw':pass1})
    if(r.text=='0'):
      #  dict = {'status': 'Username or Password incorrect'}
      messages.info(request, 'Username or Password incorrect')
      return HttpResponseRedirect(reverse('login'))
       # return render(request, 'login.html',  dict)
    else:
        return HttpResponse(r.text)
    #excep

def registration(request):
    return render(request,'registration.html',{})

def register(request):

    name=request.POST['name']
    email1=request.POST['email']
    password1=request.POST['pass']
    re_pass=request.POST['re_pass']


    if(password1==re_pass):
        r = requests.get('http://localhost/messenger/3.php', params={'type': 'register', 'e_id': email1, 'pw': password1,'name':name})
        messages.info(request,'Registration Succesful')
        #return HttpResponse(r.text)
    else:
        messages.info(request, 'password does not match')
        dict = {'status': 'password does not match'}
    return HttpResponseRedirect(reverse('login'))
def test(request):
    r=requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': 'abc@xyz.com'})
    x=json.loads(r.text)
    return HttpResponse(x['id'])


# Cre3ate    your views here.
