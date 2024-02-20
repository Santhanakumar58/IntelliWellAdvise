from django.urls import path
from .views import  list_girigless_data, create_girigless_data,update_girigless_data, delete_girigless_data, detail_girigless_data

app_name = 'girigless'

urlpatterns = [ 
    path('', list_girigless_data, name='list_girigless_data'),    
    path('create/', create_girigless_data, name='create_girigless_data'),
    path('<int:id>/update/', update_girigless_data, name='update_girigless_data'),   
    path('<int:id>/delete/', delete_girigless_data, name='delete_girigless_data'),
    path('<int:id>/detail/', detail_girigless_data, name='detail_girigless_data'),
]