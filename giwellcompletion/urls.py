from django.urls import path
from  .views import list_gicompletion_data, create_gicompletion_data, update_gicompletion_data, delete_gicompletion_data

app_name = 'giwellcompletion'

urlpatterns = [
    path('', list_gicompletion_data, name='list_gicompletion_data'),   
    path('create/', create_gicompletion_data, name='create_gicompletion_data'),
    path('<int:id>/update/', update_gicompletion_data, name='update_gicompletion_data'),
    path('<int:id>/delete/',delete_gicompletion_data, name='delete_gicompletion_data'),  
]