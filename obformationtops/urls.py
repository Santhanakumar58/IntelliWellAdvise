from django.urls import path
from .views import list_obformationtops, create_obformationtops, update_obformationtops,delete_obformationtops

app_name = 'obformationtops'

urlpatterns = [  
    path('', list_obformationtops, name='list_obformationtops'),
    path('create/', create_obformationtops, name='create_obformationtops'),
    path('<int:id>/update/', update_obformationtops, name='update_obformationtops'),    
    path('<int:id>/delete/',delete_obformationtops, name='delete_obformationtops'),
]