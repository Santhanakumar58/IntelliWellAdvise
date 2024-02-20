from django.urls import path
from .views import  list_girig_workover_data, create_girig_workover_data,update_girig_workover_data, delete_girig_workover_data, detail_girig_workover_data, intervention_home

app_name = 'girigworkover'

urlpatterns = [ 
    path('', list_girig_workover_data, name='list_girig_workover_data'),    
    path('create/', create_girig_workover_data, name='create_girig_workover_data'),
    path('<int:id>/update/', update_girig_workover_data, name='update_girig_workover_data'),   
    path('<int:id>/delete/', delete_girig_workover_data, name='delete_girig_workover_data'),
    path('intervention_home', intervention_home, name='intervention_home')
]
