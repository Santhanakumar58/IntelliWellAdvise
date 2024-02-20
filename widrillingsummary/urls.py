from django.urls import path
from  .views import list_widrillingsummary, create_widrillingsummary, update_widrillingsummary, delete_widrillingsummary

app_name = 'widrillingsummary'

urlpatterns = [
    path('', list_widrillingsummary, name='list_widrillingsummary'),   
    path('create/', create_widrillingsummary, name='create_widrillingsummary'),
    path('<int:id>/update/', update_widrillingsummary, name='update_widrillingsummary'),
    path('<int:id>/delete/',delete_widrillingsummary, name='delete_widrillingsummary'), 
]