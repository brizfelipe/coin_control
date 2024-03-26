# myapp/urls.py
from django.urls import path, include
from . import views

app_name = 'bank'

urlpatterns = [
    path('',views.index,name='index'),
    path('ajax/create_bank',views.ajax_create_bank,name='create_bank'),
    path('ajax/ajax_get_bank',views.ajax_get_banks,name='ajax_get_bank'),
    path('ajax/ajax_delete_bank/<int:id>',views.ajax_delete_bank,name='ajax_delete_bank'),
    path('ajax/ajax_update_bank',views.ajax_udpate_bank,name='ajax_udpate_bank'),

]
