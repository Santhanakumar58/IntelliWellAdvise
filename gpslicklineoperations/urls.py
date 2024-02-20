from django.urls import path
from .views import  list_gpslickline_ops_data, create_gpslickline_ops_data,update_gpslickline_ops_data, delete_gpslickline_ops_data

app_name = 'gpslicklineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_gpslickline_ops_data, name='list_gpslickline_ops_data'),    
    path('<int:ctid>/create/', create_gpslickline_ops_data, name='create_gpslickline_ops_data'),
    path('<int:id>/update/', update_gpslickline_ops_data, name='update_gpslickline_ops_data'), 
    path('<int:id>/delete/', delete_gpslickline_ops_data, name='delete_rigless_ops_data'),  
   ]