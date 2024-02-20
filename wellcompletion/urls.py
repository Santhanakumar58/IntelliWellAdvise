from django.urls import path
from  .views import list_completion_data, create_completion_data, update_completion_data, delete_completion_data

app_name = 'wellcompletion'

urlpatterns = [
    path('', list_completion_data, name='list_completion_data'),   
    path('create/', create_completion_data, name='create_completion_data'),
    path('<int:id>/update/', update_completion_data, name='update_completion_data'),
    path('<int:id>/delete/',delete_completion_data, name='delete_completion_data'),  
]