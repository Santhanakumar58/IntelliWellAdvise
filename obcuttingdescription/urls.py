from django.urls import path
from .views import list_obcutting, create_obcutting, update_obcutting, delete_obcutting

app_name = 'obcuttingdescription'

urlpatterns = [  
    path('',list_obcutting, name='list_obcutting'),
    path('create/', create_obcutting, name='create_obcutting'),
    path('<int:id>/update/', update_obcutting, name='update_obcutting'),
    path('<int:id>/delete/', delete_obcutting, name='delete_obcutting'), 

]
    