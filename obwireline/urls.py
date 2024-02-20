from django.urls import path
from  .views import list_obwireline_data, create_obwireline_data, update_obwireline_data, delete_obwireline_data, detail_obwireline_data

app_name = 'obwireline'

urlpatterns = [
    path('', list_obwireline_data, name='list_obwireline_data'),   
    path('create/', create_obwireline_data, name='create_obwireline_data'),
    path('<int:id>/update/', update_obwireline_data, name='update_obwireline_data'),
    path('<int:id>/delete/',delete_obwireline_data, name='delete_obwireline_data'),
    path('<int:id>/detail/',detail_obwireline_data, name='detail_obwireline_data'),
  
]