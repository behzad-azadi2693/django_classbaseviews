from django.urls import path
from django.contrib.auth import views as auth_views#path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
from .views import(
        PasswordConfirm, UserPassReset, UserLogin,
        PasswordResetDone, PasswordResetComplete,UserProfile
)
app_name = 'accounts'


urlpatterns =[
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/', UserPassReset.as_view(), name='reset'),
    path('reset/done/', PasswordResetDone.as_view(), name = 'password-reset-done'),
    path('confirm/<uidb64>/<token>/', PasswordConfirm.as_view(), name = 'password-confirm'),
    path('confirm/done/', PasswordResetComplete.as_view(), name = 'resaet-done'),
    path('userprofile/', UserProfile.as_view())
]
