from django.urls import path
from giinflow.views import list_giinflow, create_giinflow, update_giinflow,delete_giinflow

app_name = 'giinflow'

urlpatterns = [  
    path('', list_giinflow, name='list_giinflow'),
    path('create/', create_giinflow, name='create_giinflow'),
    path('<int:id>/update/', update_giinflow, name='update_giinflow'),   
    path('<int:id>/delete/', delete_giinflow, name='delete_giinflow'),
]