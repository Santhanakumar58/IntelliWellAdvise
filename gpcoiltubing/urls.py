from django.urls import path
from .views import  list_gpcoil_tubing_data, create_gpcoil_tubing_data,update_gpcoil_tubing_data, delete_gpcoil_tubing_data,detail_gpcoil_tubing_data


app_name = 'gpcoiltubing'

urlpatterns = [ 
    path('', list_gpcoil_tubing_data, name='list_gpcoil_tubing_data'),    
    path('create/', create_gpcoil_tubing_data, name='create_gpcoil_tubing_data'),
    path('<int:id>/update/', update_gpcoil_tubing_data, name='update_gpcoil_tubing_data'),   
    path('<int:id>/delete/', delete_gpcoil_tubing_data, name='delete_gpcoil_tubing_data'),
    path('<int:id>/detail/', detail_gpcoil_tubing_data, name='detail_gpcoil_tubing_data'),
   
   
]