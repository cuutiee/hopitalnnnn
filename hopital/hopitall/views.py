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
from hopitall.detection import FaceRecognition
from django.contrib.auth import authenticate, login

faceRecognition = FaceRecognition()

def login_cam():
    print("test")
    face_id = faceRecognition.recognizeFace()
    print(face_id)

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
                id=account.id
                print(id)
                addFace(id)
            else:
                data = serializer.errors
                print(data)
        elif 'signin' in request.POST:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('authentification/')
                   
              
                   

    return render(request, 'login_sign.html', {})

 
def addFace(face_id):
    face_id = face_id
    print(face_id)
    faceRecognition.faceDetect(face_id)
    print("detection")
    faceRecognition.trainFace()
    print("train")
    return redirect('/')

def authentification(request):
    if request.method == 'POST': 
        login_cam()
        return render(request, 'index.html', {})        

    return render(request, 'authentification.html', {})        

