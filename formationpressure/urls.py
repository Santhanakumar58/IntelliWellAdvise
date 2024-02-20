from django.urls import path
from .views import list_formation_Pressure, create_formation_Pressure, update_formation_Pressure, delete_formation_Pressure

app_name = 'formationpressure'

urlpatterns = [  
    path('',list_formation_Pressure, name='list_formation_Pressure'),
    path('create/', create_formation_Pressure, name='create_formation_Pressure'),
    path('<int:id>/update/', update_formation_Pressure, name='update_formation_Pressure'),
    path('<int:id>/delete/', delete_formation_Pressure, name='delete_formation_Pressure'), 

]
    