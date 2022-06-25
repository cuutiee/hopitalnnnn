
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('doctors/', views.doctors, name="doctors"),
    path('login_sign/', views.login_sign, name="login_sign"),
    path('login_sign/authentification/', views.authentification, name="authentification"),
]
