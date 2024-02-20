from django.urls import path
from .views import  list_widrilling_ops, create_widrilling_ops,update_widrilling_ops, delete_widrilling_ops

app_name = 'widrillingoperations'

urlpatterns = [ 
    path(r'',list_widrilling_ops, name='list_widrilling_ops'),    
    path(r'create/', create_widrilling_ops, name='create_widrilling_ops'),
    path(r'<int:id>/update/', update_widrilling_ops, name='update_widrilling_ops'), 
    path(r'<int:id>/delete/', delete_widrilling_ops, name='delete_widrilling_ops'),  
   ]