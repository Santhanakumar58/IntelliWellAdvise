from django.urls import path
from .views import  list_rigless_data, create_rigless_data,update_rigless_data, delete_rigless_data, detail_rigless_data

app_name = 'rigless'

urlpatterns = [ 
    path('', list_rigless_data, name='list_rigless_data'),    
    path('create/', create_rigless_data, name='create_rigless_data'),
    path('<int:id>/update/', update_rigless_data, name='update_rigless_data'),   
    path('<int:id>/delete/', delete_rigless_data, name='delete_rigless_data'),
    path('<int:id>/detail/', detail_rigless_data, name='detail_rigless_data'),
]