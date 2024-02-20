from django.urls import path
from wiinflow.views import list_wiinflow, create_wiinflow, update_wiinflow,delete_wiinflow

app_name = 'wiinflow'

urlpatterns = [  
    path('', list_wiinflow, name='list_wiinflow'),
    path('create/', create_wiinflow, name='create_wiinflow'),
    path('<int:id>/update/', update_wiinflow, name='update_wiinflow'),   
    path('<int:id>/delete/', delete_wiinflow, name='delete_wiinflow'),
]