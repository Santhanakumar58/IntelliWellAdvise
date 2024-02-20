from django.urls import path
from .views import  list_wicoil_tubing_data, create_wicoil_tubing_data,update_wicoil_tubing_data, delete_wicoil_tubing_data,detail_wicoil_tubing_data


app_name = 'wicoiltubing'

urlpatterns = [ 
    path('', list_wicoil_tubing_data, name='list_wicoil_tubing_data'),    
    path('create/', create_wicoil_tubing_data, name='create_wicoil_tubing_data'),
    path('<int:id>/update/', update_wicoil_tubing_data, name='update_wicoil_tubing_data'),   
    path('<int:id>/delete/', delete_wicoil_tubing_data, name='delete_wicoil_tubing_data'),
    path('<int:id>/detail/', detail_wicoil_tubing_data, name='detail_wicoil_tubing_data'),
   
   
]