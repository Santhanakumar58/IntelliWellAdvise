from django.urls import path
from .views import  list_widrilling_plan, create_widrilling_plan,update_widrilling_plan, delete_widrilling_plan

app_name = 'widrillingplanvsactual'

urlpatterns = [ 
    path('', list_widrilling_plan, name='list_widrilling_plan'),    
    path('create/', create_widrilling_plan, name='create_widrilling_plan'),
    path('<int:id>/update/', update_widrilling_plan, name='update_widrilling_plan'), 
    path('<int:id>/delete/', delete_widrilling_plan, name='delete_widrilling_plan'),  
   ]