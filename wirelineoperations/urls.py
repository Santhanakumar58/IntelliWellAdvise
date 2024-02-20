from django.urls import path
from .views import  list_wireline_ops_data, create_wireline_ops_data,update_wireline_ops_data, delete_wireline_ops_data

app_name = 'wirelineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_wireline_ops_data, name='list_wireline_ops_data'),    
    path('<int:ctid>/create/', create_wireline_ops_data, name='create_wireline_ops_data'),
    path('<int:id>/update/', update_wireline_ops_data, name='update_wireline_ops_data'), 
    path('<int:id>/delete/', delete_wireline_ops_data, name='delete_wireline_ops_data'),  
   ]