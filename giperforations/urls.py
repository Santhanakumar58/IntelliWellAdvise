from django.urls import path
from .views import list_giperforation, create_giperforation, update_giperforation, delete_giperforation

app_name = 'giperforations'

urlpatterns = [  
    path('',list_giperforation, name='list_giperforation'),
    path('create/', create_giperforation, name='create_giperforation'),
    path('<int:id>/update/', update_giperforation, name='update_giperforation'),
    path('<int:id>/delete/', delete_giperforation, name='delete_giperforation'), 

]