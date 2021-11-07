from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PersonForm


# Create your views here.
class homeView(View):
    persons = Person.objects.all()
    print(persons)
    for person in persons:
        print(person)
        print(person.username)
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
        form = PersonForm(request.POST)

        if form.is_valid():
            fname = request.POST.get("firstName")
            lname = request.POST.get("lastName")
            email = request.POST.get("email")
            uname = request.POST.get("username")
            passw = request.POST.get("password")
            cpassw = request.POST.get("confirm_password")
            gndr = request.POST.get("gender")

            
            if passw == cpassw:
                if Person.objects.filter(username=uname).exists():
                    messages.error(request,'Username already taken', extra_tags = 'user_error')
                    return redirect('register.html')
                elif Person.objects.filter(email=email).exists():
                    messages.error(request, 'Email already used', extra_tags = 'user_error')
                    return redirect('register.html')
                else:
                    form = Person(firstName=fname, lastName=lname, email=email, username=uname, password=passw, gender=gndr)
                    form.save()
            else:
                messages.error(request, 'Password does not match!', extra_tags = 'password_error')

            messages.success(request,'The user has been successfully registered!', extra_tags = 'successful')
            return render(request, 'register.html')
        else:
            messages.error(request, 'Register unsuccessful', extra_tags = 'password_error')
            return redirect('emobot:register')

        # if request.method == 'POST':
        #     form = PersonForm(request.POST)      
        #     password = request.POST.get("password")
        #     confirm_password = request.POST.get("confirm_password")
        #     if (password != confirm_password ):
        #         messages.error(request, 'Password does not match!', extra_tags = 'password_error')
        #     elif form.is_valid():
        #         form.save()
        #         messages.success(request,'The user has been successfully registered!', extra_tags = 'successful')
        #     return render(request, 'register.html')

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