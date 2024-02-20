from django.urls import path
from .views import  list_wiwireline_ops_data, create_wiwireline_ops_data,update_wiwireline_ops_data, delete_wiwireline_ops_data

app_name = 'wiwirelineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_wiwireline_ops_data, name='list_wiwireline_ops_data'),    
    path('<int:ctid>/create/', create_wiwireline_ops_data, name='create_wiwireline_ops_data'),
    path('<int:id>/update/', update_wiwireline_ops_data, name='update_wiwireline_ops_data'), 
    path('<int:id>/delete/', delete_wiwireline_ops_data, name='delete_wiwireline_ops_data'),  
   ]