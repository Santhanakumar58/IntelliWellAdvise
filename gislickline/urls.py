from django.urls import path
from  .views import list_gislickline_data, create_gislickline_data, update_gislickline_data, delete_gislickline_data, detail_gislickline_data

app_name = 'gislickline'

urlpatterns = [
    path('', list_gislickline_data, name='list_gislickline_data'),   
    path('create/', create_gislickline_data, name='create_gislickline_data'),
    path('<int:id>/update/', update_gislickline_data, name='update_gislickline_data'),
    path('<int:id>/delete/',delete_gislickline_data, name='delete_gislickline_data'),  
    path('<int:id>/detail/', detail_gislickline_data, name='detail_gislickline_data')
]