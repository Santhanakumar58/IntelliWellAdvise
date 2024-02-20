from django.urls import path
from  .views import list_stimulation_data, create_stimulation_data, update_stimulation_data, delete_stimulation_data, detail_stimulation_data

app_name = 'stimulation'

urlpatterns = [
    path('', list_stimulation_data, name='list_stimulation_data'),   
    path('create/', create_stimulation_data, name='create_stimulation_data'),
    path('<int:id>/update/', update_stimulation_data, name='update_stimulation_data'),
    path('<int:id>/delete/',delete_stimulation_data, name='delete_stimulation_data'),  
    path('<int:id>/detail/', detail_stimulation_data, name='detail_stimulation_data')
]