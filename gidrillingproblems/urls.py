from django.urls import path
from .views import  list_gidrilling_problem, create_gidrilling_problem,update_gidrilling_problem, delete_gidrilling_problem

app_name = 'gidrillingproblems'

urlpatterns = [ 
    path('', list_gidrilling_problem, name='list_gidrilling_problem'),    
    path('create/', create_gidrilling_problem, name='create_gidrilling_problem'),
    path('<int:id>/update/', update_gidrilling_problem, name='update_gidrilling_problem'), 
    path('<int:id>/delete/', delete_gidrilling_problem, name='delete_gidrilling_problem'),  
   ]