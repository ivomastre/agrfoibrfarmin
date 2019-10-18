from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="accounts"

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('forgotP/', views.forgotP, name='forgotP'),
    path('forgotE/', views.forgotE, name='forgotE'),
    path('logout_user/', views.logout_user, name='logout_user'),
]