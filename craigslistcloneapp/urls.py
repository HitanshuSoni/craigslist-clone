from django.urls import  path,re_path
from  . import views

urlpattern = [
    path('', views.home, name='home')   
]