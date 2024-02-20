from django.urls import path
from .views import  list_gprigless_ops_data, create_gprigless_ops_data,update_gprigless_ops_data, delete_gprigless_ops_data

app_name = 'gpriglessoperations'

urlpatterns = [ 
    path('<int:ctid>', list_gprigless_ops_data, name='list_gprigless_ops_data'),    
    path('<int:ctid>/create/', create_gprigless_ops_data, name='create_gprigless_ops_data'),
    path('<int:id>/update/', update_gprigless_ops_data, name='update_gprigless_ops_data'), 
    path('<int:id>/delete/', delete_gprigless_ops_data, name='delete_gprigless_ops_data'),  
   ]