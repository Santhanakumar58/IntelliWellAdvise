from django.urls import path
from .views import  list_gpdrilling_ops, create_gpdrilling_ops,update_gpdrilling_ops, delete_gpdrilling_ops

app_name = 'gpdrillingoperations'

urlpatterns = [ 
    path(r'',list_gpdrilling_ops, name='list_gpdrilling_ops'),    
    path(r'create/', create_gpdrilling_ops, name='create_gpdrilling_ops'),
    path(r'<int:id>/update/', update_gpdrilling_ops, name='update_gpdrilling_ops'), 
    path(r'<int:id>/delete/', delete_gpdrilling_ops, name='delete_gpdrilling_ops'),  
   ]