from django.urls import path
from  .views import list_gpslickline_data, create_gpslickline_data, update_gpslickline_data, delete_gpslickline_data, detail_gpslickline_data

app_name = 'gpslickline'

urlpatterns = [
    path('', list_gpslickline_data, name='list_gpslickline_data'),   
    path('create/', create_gpslickline_data, name='create_gpslickline_data'),
    path('<int:id>/update/', update_gpslickline_data, name='update_gpslickline_data'),
    path('<int:id>/delete/',delete_gpslickline_data, name='delete_gpslickline_data'),  
    path('<int:id>/detail/', detail_gpslickline_data, name='detail_gpslickline_data')
]