from django.urls import path
from .views import  list_wirig_wor_ops_data, create_wirig_wor_ops_data,update_wirig_wor_ops_data, delete_wirig_wor_ops_data

app_name = 'wiwirigworkoveroperations'

urlpatterns = [ 
    path('<int:ctid>', list_wirig_wor_ops_data, name='list_wirig_wor_ops_data'),    
    path('<int:ctid>/create/', create_wirig_wor_ops_data, name='create_wirig_wor_ops_data'),
    path('<int:id>/update/', update_wirig_wor_ops_data, name='update_wirig_wor_ops_data'), 
    path('<int:id>/delete/', delete_wirig_wor_ops_data, name='delete_wirig_wor_ops_data'),  
   ]