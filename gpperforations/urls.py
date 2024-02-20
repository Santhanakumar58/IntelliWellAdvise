from django.urls import path
from .views import list_gpperforation, create_gpperforation, update_gpperforation, delete_gpperforation

app_name = 'gpperforations'

urlpatterns = [  
    path('',list_gpperforation, name='list_gpperforation'),
    path('create/', create_gpperforation, name='create_gpperforation'),
    path('<int:id>/update/', update_gpperforation, name='update_gpperforation'),
    path('<int:id>/delete/', delete_gpperforation, name='delete_gpperforation'), 

]