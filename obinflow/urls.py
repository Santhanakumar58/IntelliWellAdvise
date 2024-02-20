from django.urls import path
from obinflow.views import list_obinflow, create_obinflow, update_obinflow,delete_obinflow

app_name = 'obinflow'

urlpatterns = [  
    path('', list_obinflow, name='list_obinflow'),
    path('create/', create_obinflow, name='create_obinflow'),
    path('<int:id>/update/', update_obinflow, name='update_obinflow'),   
    path('<int:id>/delete/', delete_obinflow, name='delete_obinflow'),
]