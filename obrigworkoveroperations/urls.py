from django.urls import path
from .views import  list_obrig_wor_ops_data, create_obrig_wor_ops_data,update_obrig_wor_ops_data, delete_obrig_wor_ops_data

app_name = 'obrigworkover1operations'

urlpatterns = [ 
    path('<int:ctid>', list_obrig_wor_ops_data, name='list_obrig_wor_ops_data'),    
    path('<int:ctid>/create/', create_obrig_wor_ops_data, name='create_obrig_wor_ops_data'),
    path('<int:id>/update/', update_obrig_wor_ops_data, name='update_obrig_wor_ops_data'), 
    path('<int:id>/delete/', delete_obrig_wor_ops_data, name='delete_obrig_wor_ops_data'),  
   ]