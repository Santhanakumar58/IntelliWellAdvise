from django.urls import path
from .views import list_gioilshow, create_gioilshow, update_gioilshow, delete_gioilshow

app_name = 'gioilshows'

urlpatterns = [  
    path('',list_gioilshow, name='list_gioilshow'),
    path('create/', create_gioilshow, name='create_gioilshow'),
    path('<int:id>/update/', update_gioilshow, name='update_gioilshow'),
    path('<int:id>/delete/', delete_gioilshow, name='delete_gioilshow'), 

]