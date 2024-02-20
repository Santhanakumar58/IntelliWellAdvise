from django.urls import path
from  .views import list_slickline_data, create_slickline_data, update_slickline_data, delete_slickline_data, detail_slickline_data

app_name = 'slickline'

urlpatterns = [
    path('', list_slickline_data, name='list_slickline_data'),   
    path('create/', create_slickline_data, name='create_slickline_data'),
    path('<int:id>/update/', update_slickline_data, name='update_slickline_data'),
    path('<int:id>/delete/',delete_slickline_data, name='delete_slickline_data'),  
    path('<int:id>/detail/', detail_slickline_data, name='detail_slickline_data')
]