from django.urls import path
from .views import list_wiformation_Pressure, create_wiformation_Pressure, update_wiformation_Pressure, delete_wiformation_Pressure

app_name = 'wiformationpressure'

urlpatterns = [  
    path('',list_wiformation_Pressure, name='list_wiformation_Pressure'),
    path('create/', create_wiformation_Pressure, name='create_wiformation_Pressure'),
    path('<int:id>/update/', update_wiformation_Pressure, name='update_wiformation_Pressure'),
    path('<int:id>/delete/', delete_wiformation_Pressure, name='delete_wiformation_Pressure'), 

]
    