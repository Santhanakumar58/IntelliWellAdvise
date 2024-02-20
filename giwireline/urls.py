from django.urls import path
from  .views import list_giwireline_data, create_giwireline_data, update_giwireline_data, delete_giwireline_data, detail_giwireline_data

app_name = 'giwireline'

urlpatterns = [
    path('', list_giwireline_data, name='list_giwireline_data'),   
    path('create/', create_giwireline_data, name='create_giwireline_data'),
    path('<int:id>/update/', update_giwireline_data, name='update_giwireline_data'),
    path('<int:id>/delete/',delete_giwireline_data, name='delete_giwireline_data'),
    path('<int:id>/detail/',detail_giwireline_data, name='detail_giwireline_data'),
  
]