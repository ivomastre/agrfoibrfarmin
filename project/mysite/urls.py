from django.urls import path, include
from . import views

app_name="mysite"

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('about_proj/', views.about_proj, name='about_proj'),
    path('test/', views.test, name='test'),
    path('show_frame/<str:name>/', views.show_frame, name='show_frame'),
]