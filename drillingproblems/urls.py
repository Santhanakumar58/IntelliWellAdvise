from django.urls import path
from .views import  list_drilling_problem, create_drilling_problem,update_drilling_problem, delete_drilling_problem

app_name = 'drillingproblems'

urlpatterns = [ 
    path('', list_drilling_problem, name='list_drilling_problem'),    
    path('create/', create_drilling_problem, name='create_drilling_problem'),
    path('<int:id>/update/', update_drilling_problem, name='update_drilling_problem'), 
    path('<int:id>/delete/', delete_drilling_problem, name='delete_drilling_problem'),  
   ]