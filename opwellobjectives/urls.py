from django.urls import path
from opwellobjectives.views import  list_opwellobjective, create_opwellobjective, update_opwellobjective,delete_opwellobjective

app_name = 'opwellobjectives'

urlpatterns = [  
    path('', list_opwellobjective, name='list_opwellobjective'),
    path('create/', create_opwellobjective, name='create_opwellobjective'),
    path('<int:id>/update/', update_opwellobjective, name='update_opwellobjective'),   
    path('<int:id>/delete/', delete_opwellobjective, name='delete_opwellobjective'),
   
   ]