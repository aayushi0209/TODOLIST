from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# from .import api/models
# Create your views here.

# ***************************************************************************************************************
#LOGIN PAGE
# ***************************************************************************************************************
def index(request):
    context = {}
    return render(request, 'frontend/login.html',context);


# ***************************************************************************************************************
# REGISTER PAGE
# ***************************************************************************************************************
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # add data to the database
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created for'+user)
    context = {'form': form}
    return render(request, 'frontend/register.html',context)
# ***************************************************************************************************************
# LOGOUT
# ***************************************************************************************************************
@login_required(login_url='/register')
def logoutuser(request):
    logout(request)
    return redirect("/")

# ***************************************************************************************************************
# AUTHENTICATION
# ***************************************************************************************************************
def login1(request):
    if request.method == "POST":
        username = request.POST.get('name1')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/list')
            else:
                print("auth failed")
                return redirect('/register')

# ***************************************************************************************************************
# list
# ***************************************************************************************************************
@login_required(login_url='/register')
def list(request):
    return render(request,"frontend/list.html")
# **************************************************************************************************************
# ************************************************************************************************************

