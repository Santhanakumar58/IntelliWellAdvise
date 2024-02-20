from django.urls import path
from .views import  list_obdrilling_plan, create_obdrilling_plan,update_obdrilling_plan, delete_obdrilling_plan

app_name = 'obdrillingplanvsactual'

urlpatterns = [ 
    path('', list_obdrilling_plan, name='list_obdrilling_plan'),    
    path('create/', create_obdrilling_plan, name='create_obdrilling_plan'),
    path('<int:id>/update/', update_obdrilling_plan, name='update_obdrilling_plan'), 
    path('<int:id>/delete/', delete_obdrilling_plan, name='delete_obdrilling_plan'),  
   ]