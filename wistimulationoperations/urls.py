from django.urls import path
from .views import  list_wistim_ops_data, create_wistim_ops_data,update_wistim_ops_data, delete_wistim_ops_data

app_name = 'wistimulationoperations'

urlpatterns = [ 
    path('<int:ctid>', list_wistim_ops_data, name='list_wistim_ops_data'),    
    path('<int:ctid>/create/', create_wistim_ops_data, name='create_wistim_ops_data'),
    path('<int:id>/update/', update_wistim_ops_data, name='update_wistim_ops_data'), 
    path('<int:id>/delete/', delete_wistim_ops_data, name='delete_wistim_ops_data'),  
   ]