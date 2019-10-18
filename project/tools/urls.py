from django.urls import path
from . import views
app_name="tools"
urlpatterns = [
    path('get_acao/', views.get_acao, name='get_acao'),
    path('get_cidade/', views.get_cidade, name='get_cidade'),
    path('tables/', views.tables, name='tables'),
]








