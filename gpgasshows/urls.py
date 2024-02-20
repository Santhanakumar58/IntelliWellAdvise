from django.urls import path
from .views import list_gpgasshow, create_gpgasshow, update_gpgasshow, delete_gpgasshow

app_name = 'gpgasshows'

urlpatterns = [  
    path('',list_gpgasshow, name='list_gpgasshow'),
    path('create/', create_gpgasshow, name='create_gpgasshow'),
    path('<int:id>/update/', update_gpgasshow, name='update_gpgasshow'),
    path('<int:id>/delete/', delete_gpgasshow, name='delete_gpgasshow'), 

]