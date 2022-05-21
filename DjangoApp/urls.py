import imp
from django.urls import path
from .views import *
urlpatterns = [
    path('',index),
    path('index/',index, name='index'),
    path('register/',register, name='register'),
    path('profiles/',profiles, name='profiles'),
]