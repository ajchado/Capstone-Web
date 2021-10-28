from django.contrib import admin
from django.urls import path
from .import views


app_name = 'emobot'

urlpatterns = [
    path('home/', views.homeView.as_view(), name="home"),
    path('dashboard/', views.dashboardView.as_view(), name="dashboard"),
    path('login/', views.loginView.as_view(), name="login"), 
    path('register/', views.registerView.as_view(), name="register"),
    path('settings/', views.settingsView.as_view(), name="settings"),
    path('user/', views.userView.as_view(), name="user"),
]