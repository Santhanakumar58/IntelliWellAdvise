from django.urls import path
from .views import  list_rig_wor_ops_data, create_rig_wor_ops_data,update_rig_wor_ops_data, delete_rig_wor_ops_data

app_name = 'rigworkoveroperations'

urlpatterns = [ 
    path('<int:ctid>', list_rig_wor_ops_data, name='list_rig_wor_ops_data'),    
    path('<int:ctid>/create/', create_rig_wor_ops_data, name='create_rig_wor_ops_data'),
    path('<int:id>/update/', update_rig_wor_ops_data, name='update_rig_wor_ops_data'), 
    path('<int:id>/delete/', delete_rig_wor_ops_data, name='delete_rig_wor_ops_data'),  
   ]