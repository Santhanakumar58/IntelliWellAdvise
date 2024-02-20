from django.urls import path
from .views import *

app_name = 'gaslift'

urlpatterns = [  
    path('', list_gas_lift, name='list_gas_lift'),
    path('create/', create_gas_lift, name='create_gas_lift'),
    path('<int:id>/update/', update_gas_lift, name='update_gas_lift'),   
    path('<int:id>/delete/', delete_gas_lift, name='delete_gas_lift'), 
    path('<int:id>/design/', design_gas_lift, name='design_gas_lift'), 
]