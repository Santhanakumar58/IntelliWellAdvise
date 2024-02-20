from django.urls import path
from .views import list_wigasshow, create_wigasshow, update_wigasshow, delete_wigasshow

app_name = 'wigasshows'

urlpatterns = [  
    path('',list_wigasshow, name='list_wigasshow'),
    path('create/', create_wigasshow, name='create_wigasshow'),
    path('<int:id>/update/', update_wigasshow, name='update_wigasshow'),
    path('<int:id>/delete/', delete_wigasshow, name='delete_wigasshow'), 

]