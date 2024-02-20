from django.urls import path
from .views import  list_obstim_ops_data, create_obstim_ops_data,update_obstim_ops_data, delete_obstim_ops_data

app_name = 'obstimulationoperations'

urlpatterns = [ 
    path('<int:ctid>', list_obstim_ops_data, name='list_obstim_ops_data'),    
    path('<int:ctid>/create/', create_obstim_ops_data, name='create_obstim_ops_data'),
    path('<int:id>/update/', update_obstim_ops_data, name='update_obstim_ops_data'), 
    path('<int:id>/delete/', delete_obstim_ops_data, name='delete_obstim_ops_data'),  
   ]