from django.urls import path
from .views import list_wicement_plug, create_wicement_plug, update_wicement_plug,delete_wicement_plug
from .views import list_wicement_pumpData, create_wicement_pumpData, update_wicement_pumpData, delete_wicement_pumpData

app_name = 'wicementplugs'

urlpatterns = [  
    path('', list_wicement_plug, name='list_wicement_plug'),
    path('create/', create_wicement_plug, name='create_wicement_plug'),
    path('<int:id>/update/', update_wicement_plug, name='update_wicement_plug'),   
    path('<int:id>/delete/', delete_wicement_plug, name='delete_wicement_plug'),
    path('<int:id>/pumpdata/', list_wicement_pumpData, name='list_wicement_pumpData'),
    path('<int:plugid>/createpumpdata/', create_wicement_pumpData, name='create_wicement_pumpData'),
    path('<int:id>/editpumpdata/', update_wicement_pumpData, name='update_wicement_pumpData'),
    path('<int:id>/deletepumpdata/', delete_wicement_pumpData, name='delete_wicement_pumpData'),
   
]