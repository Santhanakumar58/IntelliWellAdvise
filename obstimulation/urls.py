from django.urls import path
from  .views import list_obstimulation_data, create_obstimulation_data, update_obstimulation_data, delete_obstimulation_data, detail_obstimulation_data

app_name = 'obstimulation'

urlpatterns = [
    path('', list_obstimulation_data, name='list_obstimulation_data'),   
    path('create/', create_obstimulation_data, name='create_obstimulation_data'),
    path('<int:id>/update/', update_obstimulation_data, name='update_obstimulation_data'),
    path('<int:id>/delete/',delete_obstimulation_data, name='delete_obstimulation_data'),  
    path('<int:id>/detail/', detail_obstimulation_data, name='detail_obstimulation_data')
]