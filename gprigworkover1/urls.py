from django.urls import path
from .views import  list_gprig_workover_data, create_gprig_workover_data,update_gprig_workover_data, delete_gprig_workover_data, detail_gprig_workover_data, intervention_home

app_name = 'gprigworkover1'

urlpatterns = [ 
    path('', list_gprig_workover_data, name='list_gprig_workover_data'),    
    path('create/', create_gprig_workover_data, name='create_gprig_workover_data'),
    path('<int:id>/update/', update_gprig_workover_data, name='update_gprig_workover_data'),   
    path('<int:id>/delete/', delete_gprig_workover_data, name='delete_gprig_workover_data'),
    path('intervention_home', intervention_home, name='intervention_home')
]
