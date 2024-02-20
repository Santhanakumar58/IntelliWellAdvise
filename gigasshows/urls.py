from django.urls import path
from .views import list_gigasshow, create_gigasshow, update_gigasshow, delete_gigasshow

app_name = 'gigasshows'

urlpatterns = [  
    path('',list_gigasshow, name='list_gigasshow'),
    path('create/', create_gigasshow, name='create_gigasshow'),
    path('<int:id>/update/', update_gigasshow, name='update_gigasshow'),
    path('<int:id>/delete/', delete_gigasshow, name='delete_gigasshow'), 

]