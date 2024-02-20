from django.urls import path
from .views import  list_rig_workover_data, create_rig_workover_data,update_rig_workover_data, delete_rig_workover_data, detail_rig_workover_data, intervention_home

app_name = 'rigworkover'

urlpatterns = [ 
    path('', list_rig_workover_data, name='list_rig_workover_data'),    
    path('create/', create_rig_workover_data, name='create_rig_workover_data'),
    path('<int:id>/update/', update_rig_workover_data, name='update_rig_workover_data'),   
    path('<int:id>/delete/', delete_rig_workover_data, name='delete_rig_workover_data'),
    path('intervention_home', intervention_home, name='intervention_home')
]
