from django.urls import path
from .views import  list_obslickline_ops_data, create_obslickline_ops_data,update_obslickline_ops_data, delete_obslickline_ops_data

app_name = 'obslicklineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_obslickline_ops_data, name='list_obslickline_ops_data'),    
    path('<int:ctid>/create/', create_obslickline_ops_data, name='create_obslickline_ops_data'),
    path('<int:id>/update/', update_obslickline_ops_data, name='update_obslickline_ops_data'), 
    path('<int:id>/delete/', delete_obslickline_ops_data, name='delete_rigless_ops_data'),  
   ]