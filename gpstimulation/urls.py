from django.urls import path
from  .views import list_gpstimulation_data, create_gpstimulation_data, update_gpstimulation_data, delete_gpstimulation_data, detail_gpstimulation_data

app_name = 'gpstimulation'

urlpatterns = [
    path('', list_gpstimulation_data, name='list_gpstimulation_data'),   
    path('create/', create_gpstimulation_data, name='create_gpstimulation_data'),
    path('<int:id>/update/', update_gpstimulation_data, name='update_gpstimulation_data'),
    path('<int:id>/delete/',delete_gpstimulation_data, name='delete_gpstimulation_data'),  
    path('<int:id>/detail/', detail_gpstimulation_data, name='detail_gpstimulation_data')
]