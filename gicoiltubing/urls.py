from django.urls import path
from .views import  list_gicoil_tubing_data, create_gicoil_tubing_data,update_gicoil_tubing_data, delete_gicoil_tubing_data,detail_gicoil_tubing_data


app_name = 'gicoiltubing'

urlpatterns = [ 
    path('', list_gicoil_tubing_data, name='list_gicoil_tubing_data'),    
    path('create/', create_gicoil_tubing_data, name='create_gicoil_tubing_data'),
    path('<int:id>/update/', update_gicoil_tubing_data, name='update_gicoil_tubing_data'),   
    path('<int:id>/delete/', delete_gicoil_tubing_data, name='delete_gicoil_tubing_data'),
    path('<int:id>/detail/', detail_gicoil_tubing_data, name='detail_gicoil_tubing_data'),
   
   
]