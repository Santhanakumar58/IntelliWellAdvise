from django.urls import path
from .views import  list_obrigless_ops_data, create_obrigless_ops_data,update_obrigless_ops_data, delete_obrigless_ops_data

app_name = 'obriglessoperations'

urlpatterns = [ 
    path('<int:ctid>', list_obrigless_ops_data, name='list_obrigless_ops_data'),    
    path('<int:ctid>/create/', create_obrigless_ops_data, name='create_obrigless_ops_data'),
    path('<int:id>/update/', update_obrigless_ops_data, name='update_obrigless_ops_data'), 
    path('<int:id>/delete/', delete_obrigless_ops_data, name='delete_obrigless_ops_data'),  
   ]