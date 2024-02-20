from django.urls import path
from .views import  list_girigless_ops_data, create_girigless_ops_data,update_girigless_ops_data, delete_girigless_ops_data

app_name = 'giriglessoperations'

urlpatterns = [ 
    path('<int:ctid>', list_girigless_ops_data, name='list_girigless_ops_data'),    
    path('<int:ctid>/create/', create_girigless_ops_data, name='create_girigless_ops_data'),
    path('<int:id>/update/', update_girigless_ops_data, name='update_girigless_ops_data'), 
    path('<int:id>/delete/', delete_girigless_ops_data, name='delete_girigless_ops_data'),  
   ]