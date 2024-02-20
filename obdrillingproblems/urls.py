from django.urls import path
from .views import  list_obdrilling_problem, create_obdrilling_problem,update_obdrilling_problem, delete_obdrilling_problem

app_name = 'obdrillingproblems'

urlpatterns = [ 
    path('', list_obdrilling_problem, name='list_obdrilling_problem'),    
    path('create/', create_obdrilling_problem, name='create_obdrilling_problem'),
    path('<int:id>/update/', update_obdrilling_problem, name='update_obdrilling_problem'), 
    path('<int:id>/delete/', delete_obdrilling_problem, name='delete_obdrilling_problem'),  
   ]