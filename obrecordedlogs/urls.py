from django.urls import path
from .views import list_obrecorded_logs, create_obrecorded_logs, update_obrecorded_logs, delete_obrecorded_logs, view_log_from_data

app_name = 'obrecordedlogs'

urlpatterns = [  
    path('',list_obrecorded_logs, name='list_obrecorded_logs'),
    path('create/', create_obrecorded_logs, name='create_obrecorded_logs'),
    path('<int:id>/update/', update_obrecorded_logs, name='update_obrecorded_logs'),
    path('<int:id>/delete/', delete_obrecorded_logs, name='delete_obrecorded_logs'),
    path('<int:id>/view_log/', view_log_from_data, name='view_log_from_data'), 

]
    