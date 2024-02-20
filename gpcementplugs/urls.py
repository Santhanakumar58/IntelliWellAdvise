from django.urls import path
from .views import list_gpcement_plug, create_gpcement_plug, update_gpcement_plug,delete_gpcement_plug
from .views import list_gpcement_pumpData, create_gpcement_pumpData, update_gpcement_pumpData, delete_gpcement_pumpData

app_name = 'gpcementplugs'

urlpatterns = [  
    path('', list_gpcement_plug, name='list_gpcement_plug'),
    path('create/', create_gpcement_plug, name='create_gpcement_plug'),
    path('<int:id>/update/', update_gpcement_plug, name='update_gpcement_plug'),   
    path('<int:id>/delete/', delete_gpcement_plug, name='delete_gpcement_plug'),
    path('<int:id>/pumpdata/', list_gpcement_pumpData, name='list_gpcement_pumpData'),
    path('<int:plugid>/createpumpdata/', create_gpcement_pumpData, name='create_gpcement_pumpData'),
    path('<int:id>/editpumpdata/', update_gpcement_pumpData, name='update_gpcement_pumpData'),
    path('<int:id>/deletepumpdata/', delete_gpcement_pumpData, name='delete_gpcement_pumpData'),
   
]