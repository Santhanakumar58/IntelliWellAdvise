from django.urls import path
from giwellobjectives.views import  list_giwellobjective, create_giwellobjective, update_giwellobjective,delete_giwellobjective

app_name = 'giwellobjectives'

urlpatterns = [  
    path('', list_giwellobjective, name='list_giwellobjective'),
    path('create/', create_giwellobjective, name='create_giwellobjective'),
    path('<int:id>/update/', update_giwellobjective, name='update_giwellobjective'),   
    path('<int:id>/delete/', delete_giwellobjective, name='delete_giwellobjective'),
   
   ]