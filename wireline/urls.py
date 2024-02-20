from django.urls import path
from  .views import list_wireline_data, create_wireline_data, update_wireline_data, delete_wireline_data, detail_wireline_data

app_name = 'wireline'

urlpatterns = [
    path('', list_wireline_data, name='list_wireline_data'),   
    path('create/', create_wireline_data, name='create_wireline_data'),
    path('<int:id>/update/', update_wireline_data, name='update_wireline_data'),
    path('<int:id>/delete/',delete_wireline_data, name='delete_wireline_data'),
    path('<int:id>/detail/',detail_wireline_data, name='detail_wireline_data'),
  
]