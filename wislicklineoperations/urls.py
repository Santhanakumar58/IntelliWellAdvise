from django.urls import path
from .views import  list_wislickline_ops_data, create_wislickline_ops_data,update_wislickline_ops_data, delete_wislickline_ops_data

app_name = 'wislicklineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_wislickline_ops_data, name='list_wislickline_ops_data'),    
    path('<int:ctid>/create/', create_wislickline_ops_data, name='create_wislickline_ops_data'),
    path('<int:id>/update/', update_wislickline_ops_data, name='update_wislickline_ops_data'), 
    path('<int:id>/delete/', delete_wislickline_ops_data, name='delete_rigless_ops_data'),  
   ]