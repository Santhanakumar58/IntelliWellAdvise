from django.urls import path
from .views import  list_obcoil_tubing_data, create_obcoil_tubing_data,update_obcoil_tubing_data, delete_obcoil_tubing_data,detail_obcoil_tubing_data


app_name = 'obcoiltubing'

urlpatterns = [ 
    path('', list_obcoil_tubing_data, name='list_obcoil_tubing_data'),    
    path('create/', create_obcoil_tubing_data, name='create_obcoil_tubing_data'),
    path('<int:id>/update/', update_obcoil_tubing_data, name='update_obcoil_tubing_data'),   
    path('<int:id>/delete/', delete_obcoil_tubing_data, name='delete_obcoil_tubing_data'),
    path('<int:id>/detail/', detail_obcoil_tubing_data, name='detail_obcoil_tubing_data'),
   
   
]