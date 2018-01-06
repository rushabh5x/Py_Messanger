from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages
import requests
import simplejson as json


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


    a=request.GET.get("id")
    if a is not None:
        return HttpResponse(a)
    r=requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': 'def@xyz.com'})
    bhindi=json.loads(r.text)
    request.session["user"]="abc@xyz.com"
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': 'abc@xyz.com'})
    r2= requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    return render(request,'xyz.html',{'my_dict':r.json,'uniq_user':r1.json(),'user_list':r2.json()})


    #return HttpResponse(r.json())
def abcd(request):
    a=request.POST.get("id")
    #return HttpResponse(a)
    r=requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': a})
    bhindi=json.loads(r.text)
    request.session["user"]="abc@xyz.com"
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': 'abc@xyz.com'})
    r2= requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    return HttpResponse(render(request,'xyz.html',{'my_dict':r.json,'uniq_user':r1.json(),'user_list':r2.json()}))


# Cre3ate    your views here.
