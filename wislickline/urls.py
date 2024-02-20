from django.urls import path
from  .views import list_wislickline_data, create_wislickline_data, update_wislickline_data, delete_wislickline_data, detail_wislickline_data

app_name = 'wislickline'

urlpatterns = [
    path('', list_wislickline_data, name='list_wislickline_data'),   
    path('create/', create_wislickline_data, name='create_wislickline_data'),
    path('<int:id>/update/', update_wislickline_data, name='update_wislickline_data'),
    path('<int:id>/delete/',delete_wislickline_data, name='delete_wislickline_data'),  
    path('<int:id>/detail/', detail_wislickline_data, name='detail_wislickline_data')
]