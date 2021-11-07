from django.contrib import admin
from django.urls import path
from .import views


app_name = 'emobot'

urlpatterns = [
    path('home/', views.homeView.as_view(), name="home"),
    path('dashboard/', views.dashboardView.as_view(), name="dashboard"),
    path('login/', views.loginView.as_view(), name="login"), 
    path('register/', views.registerView.as_view(), name="register"),
    path('user/', views.userView.as_view(), name="user"),
    path('settings/account-settings', views.accountsettingsView.as_view(), name="account-settings"),
    path('settings/change-password', views.changepasswordView.as_view(), name="change-password"),
    path('settings/public-profile', views.publicprofileView.as_view(), name="public-profile"),
    path('settings/account-settings/delete-account', views.deleteaccountsView.as_view(), name="delete-account"),
]