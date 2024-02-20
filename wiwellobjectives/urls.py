from django.urls import path
from wiwellobjectives.views import  list_wiwellobjective, create_wiwellobjective, update_wiwellobjective,delete_wiwellobjective

app_name = 'wiwellobjectives'

urlpatterns = [  
    path('', list_wiwellobjective, name='list_wiwellobjective'),
    path('create/', create_wiwellobjective, name='create_wiwellobjective'),
    path('<int:id>/update/', update_wiwellobjective, name='update_wiwellobjective'),   
    path('<int:id>/delete/', delete_wiwellobjective, name='delete_wiwellobjective'),
   
   ]