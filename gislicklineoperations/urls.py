from django.urls import path
from .views import  list_gislickline_ops_data, create_gislickline_ops_data,update_gislickline_ops_data, delete_gislickline_ops_data

app_name = 'gislicklineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_gislickline_ops_data, name='list_gislickline_ops_data'),    
    path('<int:ctid>/create/', create_gislickline_ops_data, name='create_gislickline_ops_data'),
    path('<int:id>/update/', update_gislickline_ops_data, name='update_gislickline_ops_data'), 
    path('<int:id>/delete/', delete_gislickline_ops_data, name='delete_rigless_ops_data'),  
   ]