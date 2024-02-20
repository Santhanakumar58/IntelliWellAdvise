from django.urls import path
from .views import  list_stim_ops_data, create_stim_ops_data,update_stim_ops_data, delete_stim_ops_data

app_name = 'stimulationoperations'

urlpatterns = [ 
    path('<int:ctid>', list_stim_ops_data, name='list_stim_ops_data'),    
    path('<int:ctid>/create/', create_stim_ops_data, name='create_stim_ops_data'),
    path('<int:id>/update/', update_stim_ops_data, name='update_stim_ops_data'), 
    path('<int:id>/delete/', delete_stim_ops_data, name='delete_stim_ops_data'),  
   ]