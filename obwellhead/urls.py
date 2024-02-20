from django.urls import path
from  .views import list_obwellhead, create_obwellhead, update_obwellhead, delete_obwellhead

app_name = 'obwellhead'

urlpatterns = [
    path('', list_obwellhead, name='list_obwellhead'),   
    path('create/', create_obwellhead, name='create_obwellhead'),
    path('<int:id>/update/', update_obwellhead, name='update_obwellhead'),
    path('<int:id>/delete/',delete_obwellhead, name='delete_obwellhead'),  
]