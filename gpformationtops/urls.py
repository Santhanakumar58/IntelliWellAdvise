from django.urls import path
from .views import list_gpformationtops, create_gpformationtops, update_gpformationtops,delete_gpformationtops

app_name = 'gpformationtops'

urlpatterns = [  
    path('', list_gpformationtops, name='list_gpformationtops'),
    path('create/', create_gpformationtops, name='create_gpformationtops'),
    path('<int:id>/update/', update_gpformationtops, name='update_gpformationtops'),    
    path('<int:id>/delete/',delete_gpformationtops, name='delete_gpformationtops'),
]