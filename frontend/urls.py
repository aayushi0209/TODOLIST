from django.urls import path
from . import views

urlpatterns=[
    path("", views.index),
    path("register/",views.register),
    path("login1/",views.login1),
    path("logoutuser/",views.logoutuser),
    path("list/",views.list,name='list'),


]