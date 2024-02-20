from django.urls import path
from gpwellobjectives.views import  list_gpwellobjective, create_gpwellobjective, update_gpwellobjective,delete_gpwellobjective

app_name = 'gpwellobjectives'

urlpatterns = [  
    path('', list_gpwellobjective, name='list_gpwellobjective'),
    path('create/', create_gpwellobjective, name='create_gpwellobjective'),
    path('<int:id>/update/', update_gpwellobjective, name='update_gpwellobjective'),   
    path('<int:id>/delete/', delete_gpwellobjective, name='delete_gpwellobjective'),
   
   ]