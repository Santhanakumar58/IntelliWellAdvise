from django.urls import path
from opinflow.views import list_inflow, create_inflow, update_inflow,delete_inflow

app_name = 'opinflow'

urlpatterns = [  
    path('', list_inflow, name='list_inflow'),
    path('create/', create_inflow, name='create_inflow'),
    path('<int:id>/update/', update_inflow, name='update_inflow'),   
    path('<int:id>/delete/', delete_inflow, name='delete_inflow'),
]