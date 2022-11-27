from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth

# Create your views here.
from pyexpat.errors import messages


def home(request):
    return  render(request,"home.html")

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are now logged in")
            return redirect('nowyou')
        else:
            mesages.error(request,'Invalid Credentials')
            return redirect('sign')
    else:
        return render(request,"sign.html")


def nowyou(request):
    return  render(request,'nowyou.html')


def cstyle(request):
    return render(request,'cstyle.html')