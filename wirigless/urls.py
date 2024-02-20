from django.urls import path
from .views import  list_wirigless_data, create_wirigless_data,update_wirigless_data, delete_wirigless_data, detail_wirigless_data

app_name = 'wirigless'

urlpatterns = [ 
    path('', list_wirigless_data, name='list_wirigless_data'),    
    path('create/', create_wirigless_data, name='create_wirigless_data'),
    path('<int:id>/update/', update_wirigless_data, name='update_wirigless_data'),   
    path('<int:id>/delete/', delete_wirigless_data, name='delete_wirigless_data'),
    path('<int:id>/detail/', detail_wirigless_data, name='detail_wirigless_data'),
]