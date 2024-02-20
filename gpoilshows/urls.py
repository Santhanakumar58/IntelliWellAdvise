from django.urls import path
from .views import list_gpoilshow, create_gpoilshow, update_gpoilshow, delete_gpoilshow

app_name = 'gpoilshows'

urlpatterns = [  
    path('',list_gpoilshow, name='list_gpoilshow'),
    path('create/', create_gpoilshow, name='create_gpoilshow'),
    path('<int:id>/update/', update_gpoilshow, name='update_gpoilshow'),
    path('<int:id>/delete/', delete_gpoilshow, name='delete_gpoilshow'), 

]