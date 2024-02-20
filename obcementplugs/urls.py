from django.urls import path
from .views import list_obcement_plug, create_obcement_plug, update_obcement_plug,delete_obcement_plug
from .views import list_obcement_pumpData, create_obcement_pumpData, update_obcement_pumpData, delete_obcement_pumpData

app_name = 'obcementplugs'

urlpatterns = [  
    path('', list_obcement_plug, name='list_obcement_plug'),
    path('create/', create_obcement_plug, name='create_obcement_plug'),
    path('<int:id>/update/', update_obcement_plug, name='update_obcement_plug'),   
    path('<int:id>/delete/', delete_obcement_plug, name='delete_obcement_plug'),
    path('<int:id>/pumpdata/', list_obcement_pumpData, name='list_obcement_pumpData'),
    path('<int:plugid>/createpumpdata/', create_obcement_pumpData, name='create_obcement_pumpData'),
    path('<int:id>/editpumpdata/', update_obcement_pumpData, name='update_obcement_pumpData'),
    path('<int:id>/deletepumpdata/', delete_obcement_pumpData, name='delete_obcement_pumpData'),
   
]