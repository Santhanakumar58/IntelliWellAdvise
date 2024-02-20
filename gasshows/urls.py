from django.urls import path
from .views import list_gasshow, create_gasshow, update_gasshow, delete_gasshow

app_name = 'gasshows'

urlpatterns = [  
    path('',list_gasshow, name='list_gasshow'),
    path('create/', create_gasshow, name='create_gasshow'),
    path('<int:id>/update/', update_gasshow, name='update_gasshow'),
    path('<int:id>/delete/', delete_gasshow, name='delete_gasshow'), 

]