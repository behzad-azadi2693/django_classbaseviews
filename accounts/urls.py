from django.urls import path
from django.contrib.auth import views as auth_views#path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
from . import views

app_name = 'accounts'


urlpatterns =[
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]