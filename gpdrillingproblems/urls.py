from django.urls import path
from .views import  list_gpdrilling_problem, create_gpdrilling_problem,update_gpdrilling_problem, delete_gpdrilling_problem

app_name = 'gpdrillingproblems'

urlpatterns = [ 
    path('', list_gpdrilling_problem, name='list_gpdrilling_problem'),    
    path('create/', create_gpdrilling_problem, name='create_gpdrilling_problem'),
    path('<int:id>/update/', update_gpdrilling_problem, name='update_gpdrilling_problem'), 
    path('<int:id>/delete/', delete_gpdrilling_problem, name='delete_gpdrilling_problem'),  
   ]