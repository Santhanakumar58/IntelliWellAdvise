from django.urls import path
from .views import  list_fluid_composition, create_fluid_composition,update_fluid_composition, delete_fluid_composition


app_name = 'reservoirfluidcomposition'

urlpatterns = [ 
    path('', list_fluid_composition, name='list_fluid_composition'),    
    path('create/', create_fluid_composition, name='create_fluid_composition'),
    path('<int:id>/update/', update_fluid_composition, name='update_fluid_composition'),   
    path('<int:id>/delete/', delete_fluid_composition, name='delete_fluid_composition'),
   ]