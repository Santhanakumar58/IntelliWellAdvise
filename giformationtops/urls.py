from django.urls import path
from .views import list_giformationtops, create_giformationtops, update_giformationtops,delete_giformationtops

app_name = 'giformationtops'

urlpatterns = [  
    path('', list_giformationtops, name='list_giformationtops'),
    path('create/', create_giformationtops, name='create_giformationtops'),
    path('<int:id>/update/', update_giformationtops, name='update_giformationtops'),    
    path('<int:id>/delete/',delete_giformationtops, name='delete_giformationtops'),
]