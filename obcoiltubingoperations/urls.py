from django.urls import path
from .views import  list_obcoil_tubing_ops_data, create_obcoil_tubing_ops_data,update_obcoil_tubing_ops_data, delete_obcoil_tubing_ops_data

app_name = 'obcoiltubingoperations'

urlpatterns = [ 
    path('<int:ctid>', list_obcoil_tubing_ops_data, name='list_obcoil_tubing_ops_data'),    
    path('<int:ctid>/create/', create_obcoil_tubing_ops_data, name='create_obcoil_tubing_ops_data'),
    path('<int:id>/update/', update_obcoil_tubing_ops_data, name='update_obcoil_tubing_ops_data'), 
    path('<int:id>/delete/', delete_obcoil_tubing_ops_data, name='delete_obcoil_tubing_ops_data'),  
   ]