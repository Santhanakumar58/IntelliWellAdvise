from django.urls import path
from .views import  list_gpcoil_tubing_ops_data, create_gpcoil_tubing_ops_data,update_gpcoil_tubing_ops_data, delete_gpcoil_tubing_ops_data

app_name = 'gpcoiltubingoperations'

urlpatterns = [ 
    path('<int:ctid>', list_gpcoil_tubing_ops_data, name='list_gpcoil_tubing_ops_data'),    
    path('<int:ctid>/create/', create_gpcoil_tubing_ops_data, name='create_gpcoil_tubing_ops_data'),
    path('<int:id>/update/', update_gpcoil_tubing_ops_data, name='update_gpcoil_tubing_ops_data'), 
    path('<int:id>/delete/', delete_gpcoil_tubing_ops_data, name='delete_gpcoil_tubing_ops_data'),  
   ]