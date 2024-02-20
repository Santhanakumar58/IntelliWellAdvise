from django.urls import path
from .views import  list_obrigless_data, create_obrigless_data,update_obrigless_data, delete_obrigless_data, detail_obrigless_data

app_name = 'obrigless'

urlpatterns = [ 
    path('', list_obrigless_data, name='list_obrigless_data'),    
    path('create/', create_obrigless_data, name='create_obrigless_data'),
    path('<int:id>/update/', update_obrigless_data, name='update_obrigless_data'),   
    path('<int:id>/delete/', delete_obrigless_data, name='delete_obrigless_data'),
    path('<int:id>/detail/', detail_obrigless_data, name='detail_obrigless_data'),
]