from django.urls import path
from .views import  list_drilling_plan, create_drilling_plan,update_drilling_plan, delete_drilling_plan

app_name = 'drillingplanvsactual'

urlpatterns = [ 
    path('', list_drilling_plan, name='list_drilling_plan'),    
    path('create/', create_drilling_plan, name='create_drilling_plan'),
    path('<int:id>/update/', update_drilling_plan, name='update_drilling_plan'), 
    path('<int:id>/delete/', delete_drilling_plan, name='delete_drilling_plan'),  
   ]