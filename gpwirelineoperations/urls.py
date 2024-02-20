from django.urls import path
from .views import  list_gpwireline_ops_data, create_gpwireline_ops_data,update_gpwireline_ops_data, delete_gpwireline_ops_data

app_name = 'gpwirelineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_gpwireline_ops_data, name='list_gpwireline_ops_data'),    
    path('<int:ctid>/create/', create_gpwireline_ops_data, name='create_gpwireline_ops_data'),
    path('<int:id>/update/', update_gpwireline_ops_data, name='update_gpwireline_ops_data'), 
    path('<int:id>/delete/', delete_gpwireline_ops_data, name='delete_gpwireline_ops_data'),  
   ]