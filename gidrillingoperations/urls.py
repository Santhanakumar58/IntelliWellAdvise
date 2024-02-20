from django.urls import path
from .views import  list_gidrilling_ops, create_gidrilling_ops,update_gidrilling_ops, delete_gidrilling_ops

app_name = 'gidrillingoperations'

urlpatterns = [ 
    path(r'',list_gidrilling_ops, name='list_gidrilling_ops'),    
    path(r'create/', create_gidrilling_ops, name='create_gidrilling_ops'),
    path(r'<int:id>/update/', update_gidrilling_ops, name='update_gidrilling_ops'), 
    path(r'<int:id>/delete/', delete_gidrilling_ops, name='delete_gidrilling_ops'),  
   ]