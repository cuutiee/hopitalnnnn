import email
from email.mime import image
from multiprocessing import context
from urllib.request import Request
from django.shortcuts import redirect, render
from django.views.generic import ListView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def login_sign(request):
    user = User()

    if request.method == 'POST':      
        if 'signup' in request.POST:
            serializer = RegistrationSerializer(data=request.POST)
            if serializer.is_valid():
                account = serializer.save(image=request.FILES['img'])
            else:
                data = serializer.errors

        elif 'signin' in request.POST:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('authentification/')
                   
              
                   

    return render(request, 'login_sign.html', {})

 

def authentification(request):
    return render(request, 'authentification.html', {})        

