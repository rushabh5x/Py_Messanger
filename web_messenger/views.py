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
        # if a is not None:
        #   return HttpResponse(a)
        r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': a, 'email1': b})

        r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
        r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
        if (not r.json()):
            request.session["msg"] = '0';
        else:
            request.session["msg"] = '1';

        return render(request, 'xyz.html',
                      {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json(), 'msg': '1'})

    return render(request,'login.html')

def validation(request):
    #if(request.session["user"] != ""):
      #  return HttpResponseRedirect(reverse('login'))
    unm1=request.POST['user']
    pass1=request.POST['pwd']
    r=requests.get('http://localhost/messenger/3.php',params={'type':'login','un':unm1,'pw':pass1})
    if(r.text=='0'):
      #  dict = {'status': 'Username or Password incorrect'}
      messages.info(request, 'Username or Password incorrect')
      return HttpResponseRedirect(reverse('login'))
       # return render(request, 'login.html',  dict)
    else:
        request.session["user"]=unm1
        a = 'jalpapatel@gmail.com'
        b = request.session["user"]
                            # if a is not None:
            #   return HttpResponse(a)
        r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': a, 'email1': b})


        r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
        r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
        if (not r.json()):
            request.session["msg"] = '0';
        else:
            request.session["msg"] = '1';

        return render(request, 'xyz.html', { 'my_dict':r.json(),'uniq_user': r1.json(), 'user_list': r2.json(), 'msg':'1'})

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
    if(request.session["user"] == ""):
        messages.info(request, 'Please login')

        return HttpResponseRedirect(reverse('login'))

    a='def@xyz.com'
    b=request.session["user"]

    if request.method == 'POST':
        a = request.POST.get("id")

    #if a is not None:

    r=requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': a , 'email1':b})
    bhindi=json.loads(r. text)
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
    r2= requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    if (not r.json()):
        request.session["msg"] = '0';
    else:
        request.session["msg"] = '1';
    return render(request,'xyz.html',{'my_dict':r.json,'uniq_user':r1.json(),'user_list':r2.json(), 'msg':'1'})


    #return HttpResponse(r.json())
def abcd(request):
    a=request.POST.get("id")
    #return HttpResponse(a)
    r=requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': a})
    bhindi=json.loads(r.text)
    request.session["user"]="abc@xyz.com"
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': 'abc@xyz.com'})
    r2= requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    return HttpResponse(render(request,'xyz.html',{'my_dict':r.json,'uniq_user':r1.json(),'user_list':r2.json(), 'msg':'1'}))

def logout(request):
    request.session["user"]="";
    request.session["msg"] = "";
    messages.info(request, 'You are sucessfully logged out')

    return HttpResponseRedirect(reverse('login'))

# Cre3ate    your views here.
def sendmessage(request):


   # receive=request.POST.get("receiver")
   # message=request.POST.get("msg")
   # b = request.session["user"]
    #r3=requests.get('http://localhost/messenger/3.php', params={'type': 'sendmessage', 'sender': b,'receiver':receive,'data':message})
    #r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': receive, 'email1': b})
    #bhindi = json.loads(r.text)
    #r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
    #r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    #return HttpResponse(
     #   render(request, 'refresh.html', {'my_dict': r.json() }))


    receive = request.POST.get("receiver")
    message = request.POST.get("msg")
    b = request.session["user"]
    r3 = requests.get('http://localhost/messenger/3.php',
                      params={'type': 'sendmessage', 'sender': b, 'receiver': receive, 'data': message})
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': receive, 'email1':b})
    bhindi = json.loads(r.text)
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
    r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})


    if (not r.json()):
        request.session["msg"] = '0';
    else:
        request.session["msg"] = '1';
    return HttpResponse(
        render(request, 'xyz.html', {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json(), 'msg':'1'}))

def delete(request):
    receive = request.session["user"]
    send=request.POST.get("id")
    r3= requests.get('http://localhost/messenger/3.php', params={'type': 'deleteallmessage', 'email': send, 'email1': receive})

    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': receive, 'email1': send})
    bhindi = json.loads(r.text)
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': receive})
    r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})
    if (not r.json()):
        request.session["msg"] = '0';
    else:
        request.session["msg"] = '1';
    return HttpResponse(
        render(request, 'xyz.html', {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json(), 'msg':'1'}))

def deletesingle(request):
    id = request.POST.get("id")
    receive = request.POST.get("name")
    b = request.session["user"]

    r3 = requests.get('http://localhost/messenger/3.php',
                      params={'type': 'deletemessage', 'id': id})
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': receive, 'email1': b})



    bhindi = json.loads(r.text)
    r1 = requests.get('http://localhost/messenger/3.php', params={'type': 'getusers', 'email': b})
    r2 = requests.get('http://localhost/messenger/3.php', params={'type': 'getuserlist'})

    if(not r.json()):
        request.session["msg"] = '0';
        return HttpResponse(
            render(request, 'xyz.html', {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json() , 'msg':'0'}))
    else:
        request.session["msg"] = '1';
        return HttpResponse(
            render(request, 'xyz.html',
                   {'my_dict': r.json(), 'uniq_user': r1.json(), 'user_list': r2.json(), 'msg': '1'}))








def autorefresh(request):
    a = request.POST.get("id")
    b = request.session["user"]
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'getmessage', 'email': a , 'email1': b})
    return HttpResponse(
        render(request, 'refresh.html', {'my_dict': r.json()}))


def updateprofile(request):
    b = request.session["user"]
    pic= request.POST.get("pic")
    location = settings.PRIVATE_STORAGE_ROOT
    #image1=request.FILES['upload']
    r = requests.post('http://localhost/messenger/3.php', data={'type': 'profilechange', 'id': b, 'pic': pic , 'path':location})
    return HttpResponse(r.text)


def random(request):
    location=settings.PRIVATE_STORAGE_ROOT
    return HttpResponse(location)
    return render(request,'img_upload.html')
    a = request.POST.get("id")

    return HttpResponse(render(request,'xyz.html'))