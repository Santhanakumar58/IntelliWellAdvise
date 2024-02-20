from django.urls import path
from  .views import list_gistimulation_data, create_gistimulation_data, update_gistimulation_data, delete_gistimulation_data, detail_gistimulation_data

app_name = 'gistimulation'

urlpatterns = [
    path('', list_gistimulation_data, name='list_gistimulation_data'),   
    path('create/', create_gistimulation_data, name='create_gistimulation_data'),
    path('<int:id>/update/', update_gistimulation_data, name='update_gistimulation_data'),
    path('<int:id>/delete/',delete_gistimulation_data, name='delete_gistimulation_data'),  
    path('<int:id>/detail/', detail_gistimulation_data, name='detail_gistimulation_data')
]