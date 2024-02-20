from django.urls import path
from .views import  list_giwireline_ops_data, create_giwireline_ops_data,update_giwireline_ops_data, delete_giwireline_ops_data

app_name = 'giwirelineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_giwireline_ops_data, name='list_giwireline_ops_data'),    
    path('<int:ctid>/create/', create_giwireline_ops_data, name='create_giwireline_ops_data'),
    path('<int:id>/update/', update_giwireline_ops_data, name='update_giwireline_ops_data'), 
    path('<int:id>/delete/', delete_giwireline_ops_data, name='delete_giwireline_ops_data'),  
   ]