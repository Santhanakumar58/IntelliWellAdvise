from django.urls import path
from .views import list_wirecorded_logs, create_wirecorded_logs, update_wirecorded_logs, delete_wirecorded_logs, view_log_from_data

app_name = 'wirecordedlogs'

urlpatterns = [  
    path('',list_wirecorded_logs, name='list_wirecorded_logs'),
    path('create/', create_wirecorded_logs, name='create_wirecorded_logs'),
    path('<int:id>/update/', update_wirecorded_logs, name='update_wirecorded_logs'),
    path('<int:id>/delete/', delete_wirecorded_logs, name='delete_wirecorded_logs'),
    path('<int:id>/view_log/', view_log_from_data, name='view_log_from_data'), 

]
    