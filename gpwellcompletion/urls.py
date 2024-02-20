from django.urls import path
from  .views import list_gpcompletion_data, create_gpcompletion_data, update_gpcompletion_data, delete_gpcompletion_data

app_name = 'gpwellcompletion'

urlpatterns = [
    path('', list_gpcompletion_data, name='list_gpcompletion_data'),   
    path('create/', create_gpcompletion_data, name='create_gpcompletion_data'),
    path('<int:id>/update/', update_gpcompletion_data, name='update_gpcompletion_data'),
    path('<int:id>/delete/',delete_gpcompletion_data, name='delete_gpcompletion_data'),  
]