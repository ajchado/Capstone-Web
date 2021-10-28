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



# Create your views here.
class homeView(View):
    def get(self, request):
        
        return render(request, 'home.html')

class dashboardView(View):
    def get(self, request):
        
        return render(request, 'dashboard.html')

# class loginView(View):
#     def get(self, request):
#         return render(request, 'login.html')

#     def post(self, request):
#         uname = request.POST.get('username')
#         pwd = request.POST.get('password')

#         if User.objects.filter(pk=uname).count() != 0:
#             account = User.objects.get(pk=uname)
            
#             if account.password == pwd:
#                 return render(request, 'home.html')
        
#         return render(request, 'login.html')

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
        form = UserForm(request.POST)       
        if form.is_valid():
            form.save()
        return render(request, 'register.html')

class settingsView(View):
    def get(self, request):
        
        return render(request, 'settings.html')

class userView(View):
    def get(self, request):
        
        return render(request, 'user.html')