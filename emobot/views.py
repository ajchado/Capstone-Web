from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
# from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.contrib import messages


# Create your views here.
class homeView(View):
    def get(self, request):
        
        return render(request, 'home.html')

class dashboardView(View):
    def get(self, request):
        
        return render(request, 'dashboard.html')

class loginView(View):

    def get(self, request):
        # form = LoginForm()
        return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username = username, password = password)

            
        return render(request, 'home.html')

class registerView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.method == 'POST':
            form = UserForm(request.POST)      
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if (password != confirm_password ):
                messages.error(request, 'Password does not match!', extra_tags = 'password_error')
            elif form.is_valid():
                form.save()
                messages.success(request,'The user has been successfully registered!', extra_tags = 'successful')
            return render(request, 'register.html')

class userView(View):
    def get(self, request):
        
        return render(request, 'user.html')

class accountsettingsView(View):
    def get(self, request):
        
        return render(request, 'account-settings.html')

class changepasswordView(View):
    def get(self, request):
        
        return render(request, 'change-password.html')

class publicprofileView(View):
    def get(self, request):
        
        return render(request, 'public-profile.html')

class deleteaccountsView(View):
    def get(self, request):
        
        return render(request, 'delete-account.html')