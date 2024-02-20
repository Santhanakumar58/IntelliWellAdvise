from django.urls import path
from .views import list_obgasshow, create_obgasshow, update_obgasshow, delete_obgasshow

app_name = 'obgasshows'

urlpatterns = [  
    path('',list_obgasshow, name='list_obgasshow'),
    path('create/', create_obgasshow, name='create_obgasshow'),
    path('<int:id>/update/', update_obgasshow, name='update_obgasshow'),
    path('<int:id>/delete/', delete_obgasshow, name='delete_obgasshow'), 

]