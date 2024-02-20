from django.urls import path
from  .views import list_obwellcompletion, create_obwellcompletion, update_obwellcompletion, delete_obwellcompletion

app_name = 'obwellcompletion'

urlpatterns = [
    path('', list_obwellcompletion, name='list_obwellcompletion'),   
    path('create/', create_obwellcompletion, name='create_obwellcompletion'),
    path('<int:id>/update/', update_obwellcompletion, name='update_obwellcompletion'),
    path('<int:id>/delete/',delete_obwellcompletion, name='delete_obwellcompletion'),  
]