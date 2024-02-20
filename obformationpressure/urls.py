from django.urls import path
from .views import list_obformation_Pressure, create_obformation_Pressure, update_obformation_Pressure,delete_obformation_Pressure

app_name = 'obformationpressure'

urlpatterns = [  
    path('', list_obformation_Pressure, name='list_obformation_Pressure'),
    path('create/', create_obformation_Pressure, name='create_obformation_Pressure'),
    path('<int:id>/update/', update_obformation_Pressure, name='update_obformation_Pressure'),    
    path('<int:id>/delete/',delete_obformation_Pressure, name='delete_obformation_Pressure'),
]