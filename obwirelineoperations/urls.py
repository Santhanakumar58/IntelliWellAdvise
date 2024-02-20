from django.urls import path
from .views import  list_obwireline_ops_data, create_obwireline_ops_data,update_obwireline_ops_data, delete_obwireline_ops_data

app_name = 'obwirelineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_obwireline_ops_data, name='list_obwireline_ops_data'),    
    path('<int:ctid>/create/', create_obwireline_ops_data, name='create_obwireline_ops_data'),
    path('<int:id>/update/', update_obwireline_ops_data, name='update_obwireline_ops_data'), 
    path('<int:id>/delete/', delete_obwireline_ops_data, name='delete_obwireline_ops_data'),  
   ]