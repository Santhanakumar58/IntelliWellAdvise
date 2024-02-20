from django.urls import path
from  .views import list_gpdrillingsummary, create_gpdrillingsummary, update_gpdrillingsummary, delete_gpdrillingsummary

app_name = 'gpdrillingsummary'

urlpatterns = [
    path('', list_gpdrillingsummary, name='list_gpdrillingsummary'),   
    path('create/', create_gpdrillingsummary, name='create_gpdrillingsummary'),
    path('<int:id>/update/', update_gpdrillingsummary, name='update_gpdrillingsummary'),
    path('<int:id>/delete/',delete_gpdrillingsummary, name='delete_gpdrillingsummary'), 
]