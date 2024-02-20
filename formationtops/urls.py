from django.urls import path
from .views import list_formationTops, create_formationTops, update_formationTops,delete_formationTops

app_name = 'formationtops'

urlpatterns = [  
    path('', list_formationTops, name='list_formationtops'),
    path('create/', create_formationTops, name='create_formationtops'),
    path('<int:id>/update/', update_formationTops, name='update_formationtops'),    
    path('<int:id>/delete/',delete_formationTops, name='delete_formationtops'),
]