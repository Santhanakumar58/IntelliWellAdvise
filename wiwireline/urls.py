from django.urls import path
from  .views import list_wiwireline_data, create_wiwireline_data, update_wiwireline_data, delete_wiwireline_data, detail_wiwireline_data

app_name = 'wiwireline'

urlpatterns = [
    path('', list_wiwireline_data, name='list_wiwireline_data'),   
    path('create/', create_wiwireline_data, name='create_wiwireline_data'),
    path('<int:id>/update/', update_wiwireline_data, name='update_wiwireline_data'),
    path('<int:id>/delete/',delete_wiwireline_data, name='delete_wiwireline_data'),
    path('<int:id>/detail/',detail_wiwireline_data, name='detail_wiwireline_data'),
  
]