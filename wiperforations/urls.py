from django.urls import path
from .views import list_wiperforation, create_wiperforation, update_wiperforation, delete_wiperforation

app_name = 'wiperforations'

urlpatterns = [  
    path('',list_wiperforation, name='list_wiperforation'),
    path('create/', create_wiperforation, name='create_wiperforation'),
    path('<int:id>/update/', update_wiperforation, name='update_wiperforation'),
    path('<int:id>/delete/', delete_wiperforation, name='delete_wiperforation'), 

]