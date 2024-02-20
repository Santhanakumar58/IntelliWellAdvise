from django.urls import path
from .views import list_recorded_logs, create_recorded_logs, update_recorded_logs, delete_recorded_logs, view_log_from_data

app_name = 'recordedlogs'

urlpatterns = [  
    path('',list_recorded_logs, name='list_recorded_logs'),
    path('create/', create_recorded_logs, name='create_recorded_logs'),
    path('<int:id>/update/', update_recorded_logs, name='update_recorded_logs'),
    path('<int:id>/delete/', delete_recorded_logs, name='delete_recorded_logs'),
    path('<int:id>/view_log/', view_log_from_data, name='view_log_from_data'), 

]
    