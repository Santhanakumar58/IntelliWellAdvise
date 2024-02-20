from django.urls import path
from .views import list_gpformation_Pressure, create_gpformation_Pressure, update_gpformation_Pressure, delete_gpformation_Pressure

app_name = 'gpformationpressure'

urlpatterns = [  
    path('',list_gpformation_Pressure, name='list_gpformation_Pressure'),
    path('create/', create_gpformation_Pressure, name='create_gpformation_Pressure'),
    path('<int:id>/update/', update_gpformation_Pressure, name='update_gpformation_Pressure'),
    path('<int:id>/delete/', delete_gpformation_Pressure, name='delete_gpformation_Pressure'), 

]
    