from django.urls import path
from  .views import list_wistimulation_data, create_wistimulation_data, update_wistimulation_data, delete_wistimulation_data, detail_wistimulation_data

app_name = 'wistimulation'

urlpatterns = [
    path('', list_wistimulation_data, name='list_wistimulation_data'),   
    path('create/', create_wistimulation_data, name='create_wistimulation_data'),
    path('<int:id>/update/', update_wistimulation_data, name='update_wistimulation_data'),
    path('<int:id>/delete/',delete_wistimulation_data, name='delete_wistimulation_data'),  
    path('<int:id>/detail/', detail_wistimulation_data, name='detail_wistimulation_data')
]