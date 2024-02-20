from django.urls import path
from .views import list_oilshow, create_oilshow, update_oilshow, delete_oilshow

app_name = 'oilshows'

urlpatterns = [  
    path('',list_oilshow, name='list_oilshow'),
    path('create/', create_oilshow, name='create_oilshow'),
    path('<int:id>/update/', update_oilshow, name='update_oilshow'),
    path('<int:id>/delete/', delete_oilshow, name='delete_oilshow'), 

]