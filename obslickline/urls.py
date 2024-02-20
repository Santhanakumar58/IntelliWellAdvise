from django.urls import path
from  .views import list_obslickline_data, create_obslickline_data, update_obslickline_data, delete_obslickline_data, detail_obslickline_data

app_name = 'obslickline'

urlpatterns = [
    path('', list_obslickline_data, name='list_obslickline_data'),   
    path('create/', create_obslickline_data, name='create_obslickline_data'),
    path('<int:id>/update/', update_obslickline_data, name='update_obslickline_data'),
    path('<int:id>/delete/',delete_obslickline_data, name='delete_obslickline_data'),  
    path('<int:id>/detail/', detail_obslickline_data, name='detail_obslickline_data')
]