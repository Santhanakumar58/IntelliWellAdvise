from django.urls import path
from .views import list_perforation, create_perforation, update_perforation, delete_perforation

app_name = 'perforations'

urlpatterns = [  
    path('',list_perforation, name='list_perforation'),
    path('create/', create_perforation, name='create_perforation'),
    path('<int:id>/update/', update_perforation, name='update_perforation'),
    path('<int:id>/delete/', delete_perforation, name='delete_perforation'), 

]