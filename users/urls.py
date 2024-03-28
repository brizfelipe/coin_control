# myapp/urls.py
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('regster',views.register,name='register'),
    path('perfil',views.perfil,name='perfil'),

]
