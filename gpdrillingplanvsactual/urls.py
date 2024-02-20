from django.urls import path
from .views import  list_gpdrilling_plan, create_gpdrilling_plan,update_gpdrilling_plan, delete_gpdrilling_plan

app_name = 'gpdrillingplanvsactual'

urlpatterns = [ 
    path('', list_gpdrilling_plan, name='list_gpdrilling_plan'),    
    path('create/', create_gpdrilling_plan, name='create_gpdrilling_plan'),
    path('<int:id>/update/', update_gpdrilling_plan, name='update_gpdrilling_plan'), 
    path('<int:id>/delete/', delete_gpdrilling_plan, name='delete_gpdrilling_plan'),  
   ]