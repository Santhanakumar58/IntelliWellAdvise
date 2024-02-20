from django.urls import path
from .views import  list_girig_wor_ops_data, create_girig_wor_ops_data,update_girig_wor_ops_data, delete_girig_wor_ops_data

app_name = 'girigworkover1operations'

urlpatterns = [ 
    path('<int:ctid>', list_girig_wor_ops_data, name='list_girig_wor_ops_data'),    
    path('<int:ctid>/create/', create_girig_wor_ops_data, name='create_girig_wor_ops_data'),
    path('<int:id>/update/', update_girig_wor_ops_data, name='update_girig_wor_ops_data'), 
    path('<int:id>/delete/', delete_girig_wor_ops_data, name='delete_girig_wor_ops_data'),  
   ]