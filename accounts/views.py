from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.views import (
        LoginView, LogoutView
    )
from first.models import Todo

class UserLogin(LoginView):
    users = User.objects.all()
    extra_context = {'users':users}
    template_name = 'accounts/login.html'
