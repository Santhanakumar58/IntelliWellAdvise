from django.urls import path
from .views import list_wiformationtops, create_wiformationtops, update_wiformationtops,delete_wiformationtops

app_name = 'wiformationtops'

urlpatterns = [  
    path('', list_wiformationtops, name='list_wiformationtops'),
    path('create/', create_wiformationtops, name='create_wiformationtops'),
    path('<int:id>/update/', update_wiformationtops, name='update_wiformationtops'),    
    path('<int:id>/delete/',delete_wiformationtops, name='delete_wiformationtops'),
]