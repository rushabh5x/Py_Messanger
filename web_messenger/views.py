from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):

    return render(request,'login.html',{})

def validation(request):
    unm1=request.POST['user']
    pass1=request.POST['password']

    return HttpResponse(unm1)
    #excep

def registration(request):
    return render(request,'registration.html',{})

def register(request):


    return HttpResponse("hello")

def test(request):
    return render(request,'test.html',{})



# Create your views here.
