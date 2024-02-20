from django.urls import path
from obwellobjectives.views import  list_obwellobjective, create_obwellobjective, update_obwellobjective,delete_obwellobjective

app_name = 'obwellobjectives'

urlpatterns = [  
    path('', list_obwellobjective, name='list_obwellobjective'),
    path('create/', create_obwellobjective, name='create_obwellobjective'),
    path('<int:id>/update/', update_obwellobjective, name='update_obwellobjective'),   
    path('<int:id>/delete/', delete_obwellobjective, name='delete_obwellobjective'),
   
   ]