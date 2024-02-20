from django.urls import path
from .views import list_gicement_plug, create_gicement_plug, update_gicement_plug,delete_gicement_plug
from .views import list_gicement_pumpData, create_gicement_pumpData, update_gicement_pumpData, delete_gicement_pumpData

app_name = 'gicementplugs'

urlpatterns = [  
    path('', list_gicement_plug, name='list_gicement_plug'),
    path('create/', create_gicement_plug, name='create_gicement_plug'),
    path('<int:id>/update/', update_gicement_plug, name='update_gicement_plug'),   
    path('<int:id>/delete/', delete_gicement_plug, name='delete_gicement_plug'),
    path('<int:id>/pumpdata/', list_gicement_pumpData, name='list_gicement_pumpData'),
    path('<int:plugid>/createpumpdata/', create_gicement_pumpData, name='create_gicement_pumpData'),
    path('<int:id>/editpumpdata/', update_gicement_pumpData, name='update_gicement_pumpData'),
    path('<int:id>/deletepumpdata/', delete_gicement_pumpData, name='delete_gicement_pumpData'),
   
]