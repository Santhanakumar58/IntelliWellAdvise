from django.urls import path
from .views import list_obperforation, create_obperforation, update_obperforation, delete_obperforation

app_name = 'obperforations'

urlpatterns = [  
    path('',list_obperforation, name='list_obperforation'),
    path('create/', create_obperforation, name='create_obperforation'),
    path('<int:id>/update/', update_obperforation, name='update_obperforation'),
    path('<int:id>/delete/', delete_obperforation, name='delete_obperforation'), 

]