from django.urls import path
from .views import  list_fluid_composition_data, create_fluid_composition_data,update_fluid_composition_data, delete_fluid_composition_data


app_name = 'reservoirfluidcompositiondata'

urlpatterns = [ 
    path('<int:fcid>/', list_fluid_composition_data, name='list_fluid_composition_data'),    
    path('<int:fcid>/create/', create_fluid_composition_data, name='create_fluid_composition_data'),
    path('<int:id>/update/', update_fluid_composition_data, name='update_fluid_composition_data'),   
    path('<int:id>/delete/', delete_fluid_composition_data, name='delete_fluid_composition_data'),
   ]