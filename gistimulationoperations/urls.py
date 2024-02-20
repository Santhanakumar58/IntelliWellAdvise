from django.urls import path
from .views import  list_gistim_ops_data, create_gistim_ops_data,update_gistim_ops_data, delete_gistim_ops_data

app_name = 'gistimulationoperations'

urlpatterns = [ 
    path('<int:ctid>', list_gistim_ops_data, name='list_gistim_ops_data'),    
    path('<int:ctid>/create/', create_gistim_ops_data, name='create_gistim_ops_data'),
    path('<int:id>/update/', update_gistim_ops_data, name='update_gistim_ops_data'), 
    path('<int:id>/delete/', delete_gistim_ops_data, name='delete_gistim_ops_data'),  
   ]