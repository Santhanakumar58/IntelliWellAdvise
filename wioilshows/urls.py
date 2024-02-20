from django.urls import path
from .views import list_wioilshow, create_wioilshow, update_wioilshow, delete_wioilshow

app_name = 'wioilshows'

urlpatterns = [  
    path('',list_wioilshow, name='list_wioilshow'),
    path('create/', create_wioilshow, name='create_wioilshow'),
    path('<int:id>/update/', update_wioilshow, name='update_wioilshow'),
    path('<int:id>/delete/', delete_wioilshow, name='delete_wioilshow'), 

]