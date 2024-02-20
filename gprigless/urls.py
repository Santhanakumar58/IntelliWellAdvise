from django.urls import path
from .views import  list_gprigless_data, create_gprigless_data,update_gprigless_data, delete_gprigless_data, detail_gprigless_data

app_name = 'gprigless'

urlpatterns = [ 
    path('', list_gprigless_data, name='list_gprigless_data'),    
    path('create/', create_gprigless_data, name='create_gprigless_data'),
    path('<int:id>/update/', update_gprigless_data, name='update_gprigless_data'),   
    path('<int:id>/delete/', delete_gprigless_data, name='delete_gprigless_data'),
    path('<int:id>/detail/', detail_gprigless_data, name='detail_gprigless_data'),
]