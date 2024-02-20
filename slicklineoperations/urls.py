from django.urls import path
from .views import  list_slickline_ops_data, create_slickline_ops_data,update_slickline_ops_data, delete_slickline_ops_data

app_name = 'slicklineoperations'

urlpatterns = [ 
    path('<int:ctid>', list_slickline_ops_data, name='list_slickline_ops_data'),    
    path('<int:ctid>/create/', create_slickline_ops_data, name='create_slickline_ops_data'),
    path('<int:id>/update/', update_slickline_ops_data, name='update_slickline_ops_data'), 
    path('<int:id>/delete/', delete_slickline_ops_data, name='delete_rigless_ops_data'),  
   ]