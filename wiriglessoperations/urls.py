from django.urls import path
from .views import  list_wirigless_ops_data, create_wirigless_ops_data,update_wirigless_ops_data, delete_wirigless_ops_data

app_name = 'wiriglessoperations'

urlpatterns = [ 
    path('<int:ctid>', list_wirigless_ops_data, name='list_wirigless_ops_data'),    
    path('<int:ctid>/create/', create_wirigless_ops_data, name='create_wirigless_ops_data'),
    path('<int:id>/update/', update_wirigless_ops_data, name='update_wirigless_ops_data'), 
    path('<int:id>/delete/', delete_wirigless_ops_data, name='delete_wirigless_ops_data'),  
   ]