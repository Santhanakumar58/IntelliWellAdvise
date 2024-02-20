from django.urls import path
from .views import list_girecorded_logs, create_girecorded_logs, update_girecorded_logs, delete_girecorded_logs, view_log_from_data

app_name = 'girecordedlogs'

urlpatterns = [  
    path('',list_girecorded_logs, name='list_girecorded_logs'),
    path('create/', create_girecorded_logs, name='create_girecorded_logs'),
    path('<int:id>/update/', update_girecorded_logs, name='update_girecorded_logs'),
    path('<int:id>/delete/', delete_girecorded_logs, name='delete_girecorded_logs'),
    path('<int:id>/view_log/', view_log_from_data, name='view_log_from_data'), 

]
    