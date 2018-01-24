from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.conf import settings
import requests
import simplejson as json
import threading



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    if(request.session["user"] != ""):
        a = 'jalpapatel@gmail.com'
        b = request.session["user"]
        r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'sender': a, 'receiver': b})
        r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
        r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
        if (not r.json()):
            request.session["msg"] = '0';
        else:
            request.session["msg"] = '1';

        return render(request, 'chatscreen.html',
                      {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json()})

    return render(request,'login.html')

def validation(request):

    unm1=request.POST['user']
    pass1=request.POST['pwd']
    r=requests.get('http://localhost/messenger/3.php',params={'type':'login','un':unm1,'pw':pass1})
    request.session["username"]=r.text
    if(r.text=='0'):
        messages.info(request, 'Username or Password incorrect')
        return HttpResponseRedirect(reverse('login'))
    else:
        request.session["user"]=unm1
        a = 'jalpapatel@gmail.com'
        b = request.session["user"]
        r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'sender': a, 'receiver': b})
        r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
        r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
        if (not r.json()):
            request.session["msg"] = '0';
        else:
            request.session["msg"] = '1';

        return render(request, 'chatscreen.html', { 'my_dict':r.json(),'uniq_user': r1.json(), 'user_list': r2.json()})



def register(request):

    name=request.POST['name']
    email1=request.POST['email']
    password1=request.POST['pass']
    re_pass=request.POST['re_pass']
    if(password1==re_pass):
        r = requests.get('http://localhost/messenger/3.php', params={'type': 'register', 'e_id': email1, 'pw': password1,'name':name})
        messages.info(request,'Registration Succesful')
    else:
        messages.info(request, 'password does not match')
    return HttpResponseRedirect(reverse('login'))

def test(request):
    if(request.session["user"] == ""):
        messages.info(request, 'Please login')
        return HttpResponseRedirect(reverse('login'))

    b=request.session["user"]

    if request.method == 'POST':
        a = request.POST.get("id")


    r=requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'sender': a , 'receiver':b})
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
    r2= requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    if (not r.json()):
        request.session["msg"] = '0';
    else:
        request.session["msg"] = '1';
    return render(request,'chatscreen.html',{'my_dict':r.json,'uniq_user':r1.json(),'user_list':r2.json()})



def logout(request):
    request.session["user"]="";
    request.session["msg"] = "";
    messages.info(request, 'You are sucessfully logged out')

    return HttpResponseRedirect(reverse('login'))


def sendmessage(request):
    receive = request.POST.get("receiver")
    message = request.POST.get("msg")
    b = request.session["user"]
    r3 = requests.get('http://localhost/messenger/3.php',
                      params={'type': 'sendmessage', 'sender': b, 'receiver': receive, 'data': message})
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'sender': receive, 'receiver':b})
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
    r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    if (not r.json()):
        request.session["msg"] = '0';
    else:
        request.session["msg"] = '1';
    return HttpResponse(
        render(request, 'chatscreen.html', {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json()}))

def delete(request):
    receive = request.session["user"]
    send=request.POST.get("id")
    r3= requests.get('http://localhost/messenger/3.php', params={'type': 'deleteallmessage', 'sender': send, 'receiver': receive})
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'sender': receive, 'receiver': send})
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': receive})
    r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    if (not r.json()):
        request.session["msg"] = '0';
    else:
        request.session["msg"] = '1';
    return HttpResponse(
        render(request, 'chatscreen.html', {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json()}))

def deletesingle(request):
    id = request.POST.get("id")
    receive = request.POST.get("name")
    b = request.session["user"]
    r3 = requests.get('http://localhost/messenger/3.php',
                      params={'type': 'deletemessage', 'id': id})
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'sender': receive, 'receiver': b})

    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
    r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})

    if(not r.json()):
        request.session["msg"] = '0';
        return HttpResponse(
            render(request, 'chatscreen.html', {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json() }))
    else:
        request.session["msg"] = '1';
        return HttpResponse(
            render(request, 'chatscreen.html',
                   {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json()}))


def autorefresh(request):
    a = request.POST.get("id")
    b = request.session["user"]
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'sender': a , 'receiver': b})
    return HttpResponse(
        render(request, 'refresh.html', {'my_dict': r.json()}))


def updateprofile(request):
    b = request.session["user"]
    pic= request.POST.get("pic")
    location = settings.PRIVATE_STORAGE_ROOT
    r = requests.post('http://localhost/messenger/3.php', data={'type': 'profilechange', 'id': b, 'pic': pic , 'path':location})
    return HttpResponse(r.text)

def changepass(request):
    if (request.session["user"] == ""):
        messages.info(request, 'Please login')
        return HttpResponseRedirect(reverse('login'))

    b=request.session["user"]
    password1=request.POST['new_pass']
    re_pass=request.POST['repass']
    if (password1 == re_pass):
        r = requests.post('http://localhost/messenger/3.php',
                          data={'type': 'changepwd', 'email': b, 'pass':password1})
    else:
        messages.info(request, 'password does not match')
        return HttpResponseRedirect(reverse('pwdchange'))


    a = 'jalpapatel@gmail.com'
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'sender': a, 'receiver': b})
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
    r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    if (not r.json()):
        request.session["msg"] = '0';
    else:
        request.session["msg"] = '1';

    return render(request, 'chatscreen.html', {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json()})

def pwdchange(request):
    if (request.session["user"] == ""):
        messages.info(request, 'Please login')
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'changepass.html')