from django.urls import path
from  .views import list_wh_data, create_wh_data, update_wh_data, delete_wh_data

app_name = 'wellhead'

urlpatterns = [
    path('', list_wh_data, name='list_wh_data'),   
    path('create/', create_wh_data, name='create_wh_data'),
    path('<int:id>/update/', update_wh_data, name='update_wh_data'),
    path('<int:id>/delete/',delete_wh_data, name='delete_wh_data'),  
]