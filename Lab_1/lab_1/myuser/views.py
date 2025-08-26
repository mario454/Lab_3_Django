from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Login(request):
    return render(request, 'myuser/login.html')

def Register(request):
    return render(request, 'myuser/register.html')

def Logout(request):
    return HttpResponse("<h1> Goodbye </h1>")
