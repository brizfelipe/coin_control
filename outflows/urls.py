# myapp/urls.py
from django.urls import path, include
from . import views

app_name = 'outflows'

urlpatterns = [
    path('',views.index,name='index'),

]
