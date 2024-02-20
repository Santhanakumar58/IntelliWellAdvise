from django.urls import path
from .views import list_wicutting, create_wicutting, update_wicutting, delete_wicutting

app_name = 'wicuttingdescription'

urlpatterns = [  
    path('',list_wicutting, name='list_wicutting'),
    path('create/', create_wicutting, name='create_wicutting'),
    path('<int:id>/update/', update_wicutting, name='update_wicutting'),
    path('<int:id>/delete/', delete_wicutting, name='delete_wicutting'), 

]
    