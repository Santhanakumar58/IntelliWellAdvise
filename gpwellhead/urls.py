from django.urls import path
from  .views import list_gpwellhead, create_gpwellhead, update_gpwellhead, delete_gpwellhead

app_name = 'gpwellhead'

urlpatterns = [
    path('', list_gpwellhead, name='list_gpwellhead'),   
    path('create/', create_gpwellhead, name='create_gpwellhead'),
    path('<int:id>/update/', update_gpwellhead, name='update_gpwellhead'),
    path('<int:id>/delete/',delete_gpwellhead, name='delete_gpwellhead'),  
]