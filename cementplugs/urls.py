from django.urls import path
from .views import list_cement_plug, create_cement_plug, update_cement_plug,delete_cement_plug
from .views import list_cement_pumpData, create_cement_pumpData, update_cement_pumpData, delete_cement_pumpData

app_name = 'cementplugs'

urlpatterns = [  
    path('', list_cement_plug, name='list_cement_plug'),
    path('create/', create_cement_plug, name='create_cement_plug'),
    path('<int:id>/update/', update_cement_plug, name='update_cement_plug'),   
    path('<int:id>/delete/', delete_cement_plug, name='delete_cement_plug'),
    path('<int:id>/pumpdata/', list_cement_pumpData, name='list_cement_pumpData'),
    path('<int:plugid>/createpumpdata/', create_cement_pumpData, name='create_cement_pumpData'),
    path('<int:id>/editpumpdata/', update_cement_pumpData, name='update_cement_pumpData'),
    path('<int:id>/deletepumpdata/', delete_cement_pumpData, name='delete_cement_pumpData'),
   
]