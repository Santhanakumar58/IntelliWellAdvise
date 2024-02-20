from django.urls import path
from .views import  list_widrilling_problem, create_widrilling_problem,update_widrilling_problem, delete_widrilling_problem

app_name = 'widrillingproblems'

urlpatterns = [ 
    path('', list_widrilling_problem, name='list_widrilling_problem'),    
    path('create/', create_widrilling_problem, name='create_widrilling_problem'),
    path('<int:id>/update/', update_widrilling_problem, name='update_widrilling_problem'), 
    path('<int:id>/delete/', delete_widrilling_problem, name='delete_widrilling_problem'),  
   ]