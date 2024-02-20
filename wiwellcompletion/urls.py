from django.urls import path
from  .views import list_wicompletion_data, create_wicompletion_data, update_wicompletion_data, delete_wicompletion_data

app_name = 'wiwellcompletion'

urlpatterns = [
    path('', list_wicompletion_data, name='list_wicompletion_data'),   
    path('create/', create_wicompletion_data, name='create_wicompletion_data'),
    path('<int:id>/update/', update_wicompletion_data, name='update_wicompletion_data'),
    path('<int:id>/delete/',delete_wicompletion_data, name='delete_wicompletion_data'),  
]