from django.urls import path
from gpinflow.views import list_gpinflow, create_gpinflow, update_gpinflow,delete_gpinflow

app_name = 'gpinflow'

urlpatterns = [  
    path('', list_gpinflow, name='list_gpinflow'),
    path('create/', create_gpinflow, name='create_gpinflow'),
    path('<int:id>/update/', update_gpinflow, name='update_gpinflow'),   
    path('<int:id>/delete/', delete_gpinflow, name='delete_gpinflow'),
]