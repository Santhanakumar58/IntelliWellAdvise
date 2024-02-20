from django.urls import path
from .views import  list_coil_tubing_ops_data, create_coil_tubing_ops_data,update_coil_tubing_ops_data, delete_coil_tubing_ops_data

app_name = 'coiltubingoperations'

urlpatterns = [ 
    path('<int:ctid>', list_coil_tubing_ops_data, name='list_coil_tubing_ops_data'),    
    path('<int:ctid>/create/', create_coil_tubing_ops_data, name='create_coil_tubing_ops_data'),
    path('<int:id>/update/', update_coil_tubing_ops_data, name='update_coil_tubing_ops_data'), 
    path('<int:id>/delete/', delete_coil_tubing_ops_data, name='delete_coil_tubing_ops_data'),  
   ]