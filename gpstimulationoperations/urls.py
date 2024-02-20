from django.urls import path
from .views import  list_gpstim_ops_data, create_gpstim_ops_data,update_gpstim_ops_data, delete_gpstim_ops_data

app_name = 'gpstimulationoperations'

urlpatterns = [ 
    path('<int:ctid>', list_gpstim_ops_data, name='list_gpstim_ops_data'),    
    path('<int:ctid>/create/', create_gpstim_ops_data, name='create_gpstim_ops_data'),
    path('<int:id>/update/', update_gpstim_ops_data, name='update_gpstim_ops_data'), 
    path('<int:id>/delete/', delete_gpstim_ops_data, name='delete_gpstim_ops_data'),  
   ]