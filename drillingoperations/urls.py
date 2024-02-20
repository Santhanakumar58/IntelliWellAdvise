from django.urls import path
from .views import  list_drilling_ops, create_drilling_ops,update_drilling_ops, delete_drilling_ops

app_name = 'drillingoperations'

urlpatterns = [ 
    path(r'',list_drilling_ops, name='list_drilling_ops'),    
    path(r'create/', create_drilling_ops, name='create_drilling_ops'),
    path(r'<int:id>/update/', update_drilling_ops, name='update_drilling_ops'), 
    path(r'<int:id>/delete/', delete_drilling_ops, name='delete_drilling_ops'),  
   ]