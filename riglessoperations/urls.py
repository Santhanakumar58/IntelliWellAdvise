from django.urls import path
from .views import  list_rigless_ops_data, create_rigless_ops_data,update_rigless_ops_data, delete_rigless_ops_data

app_name = 'riglessoperations'

urlpatterns = [ 
    path('<int:ctid>', list_rigless_ops_data, name='list_rigless_ops_data'),    
    path('<int:ctid>/create/', create_rigless_ops_data, name='create_rigless_ops_data'),
    path('<int:id>/update/', update_rigless_ops_data, name='update_rigless_ops_data'), 
    path('<int:id>/delete/', delete_rigless_ops_data, name='delete_rigless_ops_data'),  
   ]