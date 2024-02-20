from django.urls import path
from .views import list_giformation_Pressure, create_giformation_Pressure, update_giformation_Pressure, delete_giformation_Pressure

app_name = 'giformationpressure'

urlpatterns = [  
    path('',list_giformation_Pressure, name='list_giformation_Pressure'),
    path('create/', create_giformation_Pressure, name='create_giformation_Pressure'),
    path('<int:id>/update/', update_giformation_Pressure, name='update_giformation_Pressure'),
    path('<int:id>/delete/', delete_giformation_Pressure, name='delete_giformation_Pressure'), 

]
    