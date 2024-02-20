from django.urls import path
from .views import  list_wicoil_tubing_ops_data, create_wicoil_tubing_ops_data,update_wicoil_tubing_ops_data, delete_wicoil_tubing_ops_data

app_name = 'wicoiltubingoperations'

urlpatterns = [ 
    path('<int:ctid>', list_wicoil_tubing_ops_data, name='list_wicoil_tubing_ops_data'),    
    path('<int:ctid>/create/', create_wicoil_tubing_ops_data, name='create_wicoil_tubing_ops_data'),
    path('<int:id>/update/', update_wicoil_tubing_ops_data, name='update_wicoil_tubing_ops_data'), 
    path('<int:id>/delete/', delete_wicoil_tubing_ops_data, name='delete_wicoil_tubing_ops_data'),  
   ]