from django.urls import path
from .views import  list_obdrilling_ops, create_obdrilling_ops,update_obdrilling_ops, delete_obdrilling_ops

app_name = 'obdrillingoperations'

urlpatterns = [ 
    path(r'',list_obdrilling_ops, name='list_obdrilling_ops'),    
    path(r'create/', create_obdrilling_ops, name='create_obdrilling_ops'),
    path(r'<int:id>/update/', update_obdrilling_ops, name='update_obdrilling_ops'), 
    path(r'<int:id>/delete/', delete_obdrilling_ops, name='delete_obdrilling_ops'),  
   ]