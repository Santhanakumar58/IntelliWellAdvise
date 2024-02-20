from django.urls import path
from .views import  list_gidrilling_plan, create_gidrilling_plan,update_gidrilling_plan, delete_gidrilling_plan

app_name = 'gidrillingplanvsactual'

urlpatterns = [ 
    path('', list_gidrilling_plan, name='list_gidrilling_plan'),    
    path('create/', create_gidrilling_plan, name='create_gidrilling_plan'),
    path('<int:id>/update/', update_gidrilling_plan, name='update_gidrilling_plan'), 
    path('<int:id>/delete/', delete_gidrilling_plan, name='delete_gidrilling_plan'),  
   ]