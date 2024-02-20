from django.urls import path
from .views import  list_gicoil_tubing_ops_data, create_gicoil_tubing_ops_data,update_gicoil_tubing_ops_data, delete_gicoil_tubing_ops_data

app_name = 'gicoiltubingoperations'

urlpatterns = [ 
    path('<int:ctid>', list_gicoil_tubing_ops_data, name='list_gicoil_tubing_ops_data'),    
    path('<int:ctid>/create/', create_gicoil_tubing_ops_data, name='create_gicoil_tubing_ops_data'),
    path('<int:id>/update/', update_gicoil_tubing_ops_data, name='update_gicoil_tubing_ops_data'), 
    path('<int:id>/delete/', delete_gicoil_tubing_ops_data, name='delete_gicoil_tubing_ops_data'),  
   ]