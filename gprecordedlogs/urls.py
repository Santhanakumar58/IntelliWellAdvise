from django.urls import path
from .views import list_gprecorded_logs, create_gprecorded_logs, update_gprecorded_logs, delete_gprecorded_logs, view_log_from_data

app_name = 'gprecordedlogs'

urlpatterns = [  
    path('',list_gprecorded_logs, name='list_gprecorded_logs'),
    path('create/', create_gprecorded_logs, name='create_gprecorded_logs'),
    path('<int:id>/update/', update_gprecorded_logs, name='update_gprecorded_logs'),
    path('<int:id>/delete/', delete_gprecorded_logs, name='delete_gprecorded_logs'),
    path('<int:id>/view_log/', view_log_from_data, name='view_log_from_data'), 

]
    