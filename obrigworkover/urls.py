from django.urls import path
from .views import  list_obrig_workover_data, create_obrig_workover_data,update_obrig_workover_data, delete_obrig_workover_data, detail_obrig_workover_data, intervention_home

app_name = 'obrigworkover'

urlpatterns = [ 
    path('', list_obrig_workover_data, name='list_obrig_workover_data'),    
    path('create/', create_obrig_workover_data, name='create_obrig_workover_data'),
    path('<int:id>/update/', update_obrig_workover_data, name='update_obrig_workover_data'),   
    path('<int:id>/delete/', delete_obrig_workover_data, name='delete_obrig_workover_data'),
    path('intervention_home', intervention_home, name='intervention_home')
]
