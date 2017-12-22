from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):

    return render(request,'login.html',{})

def validation(request):
    unm1=request.POST['user']
    pass1=request.POST['password']
    r=requests.get('http://localhost/messenger/3.php',params={'type':'login','un':unm1,'pw':pass1})
    return HttpResponse(r.text)
    #excep

def registration(request):
    return render(request,'registration.html',{})

def register(request):

    fnm1=request.POST['fnm']
    lnm1=request.POST['lnm']
    email1=request.POST['email']
    password1=request.POST['pass']
    r = requests.get('http://localhost/messenger/3.php', params={'type': 'register', 'e_id': email1, 'pw': password1,'f_name':fnm1,'l_name':lnm1})
    return HttpResponse(r.text)

def test(request):
    return render(request,'test.html',{})



# Create your views here.
