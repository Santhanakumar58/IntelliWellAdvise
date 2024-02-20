from django.urls import path
from .views import  list_wirig_workover_data, create_wirig_workover_data,update_wirig_workover_data, delete_wirig_workover_data, detail_wirig_workover_data, wiintervention_home

app_name = 'wirigworkover'

urlpatterns = [ 
    path('', list_wirig_workover_data, name='list_wirig_workover_data'),    
    path('create/', create_wirig_workover_data, name='create_wirig_workover_data'),
    path('<int:id>/update/', update_wirig_workover_data, name='update_wirig_workover_data'),   
    path('<int:id>/delete/', delete_wirig_workover_data, name='delete_wirig_workover_data'),
    path('intervention_home', wiintervention_home, name='wiintervention_home')
]
