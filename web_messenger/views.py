from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):

    return render(request,'login.html',{})

def validation(request):
    unm1=request.POST['user']
    pass1=request.POST['pwd']
    r=requests.get('http://localhost/messenger/3.php',params={'type':'login','un':unm1,'pw':pass1})
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
        return HttpResponse(r.text)
    else:
        dict = {'status': 'password does not match'}
        return HttpResponse(render(request, 'login.html', {'data': dict}))
def test(request):
    return render(request,'test.html',{})



# Create your views here.
