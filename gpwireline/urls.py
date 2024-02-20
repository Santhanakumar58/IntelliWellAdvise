from django.urls import path
from  .views import list_gpwireline_data, create_gpwireline_data, update_gpwireline_data, delete_gpwireline_data, detail_gpwireline_data

app_name = 'gpwireline'

urlpatterns = [
    path('', list_gpwireline_data, name='list_gpwireline_data'),   
    path('create/', create_gpwireline_data, name='create_gpwireline_data'),
    path('<int:id>/update/', update_gpwireline_data, name='update_gpwireline_data'),
    path('<int:id>/delete/',delete_gpwireline_data, name='delete_gpwireline_data'),
    path('<int:id>/detail/',detail_gpwireline_data, name='detail_gpwireline_data'),
  
]