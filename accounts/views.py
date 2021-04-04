from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import (
        LoginView, LogoutView, PasswordResetView,
        PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
    )
from first.models import Todo

class UserLogin(LoginView):
    users = User.objects.all()
    extra_context = {'users':users}
    template_name = 'accounts/login.html'


class UserPassReset(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('acccounts:password-reset-done')
    html_email_template_name = 'accounts/password_reset_email.html'


class PasswordResetDone(PasswordResetDoneView):
    template_name='accounts/reset_done.html'


class PasswordConfirm(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


class UserProfile(generic.UpdateView):
    model = User
    template_name = 'polls/user.html'
    fields = ['first_name', 'last_name'] 

    def get_object(self):
        return User.objects.get(username= self.request.user.username)
