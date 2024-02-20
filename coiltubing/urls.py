from django.urls import path
from .views import  list_coil_tubing_data, create_coil_tubing_data,update_coil_tubing_data, delete_coil_tubing_data,detail_coil_tubing_data


app_name = 'coiltubing'

urlpatterns = [ 
    path('', list_coil_tubing_data, name='list_coil_tubing_data'),    
    path('create/', create_coil_tubing_data, name='create_coil_tubing_data'),
    path('<int:id>/update/', update_coil_tubing_data, name='update_coil_tubing_data'),   
    path('<int:id>/delete/', delete_coil_tubing_data, name='delete_coil_tubing_data'),
    path('<int:id>/detail/', detail_coil_tubing_data, name='detail_coil_tubing_data'),
   
   
]