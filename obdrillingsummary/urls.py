from django.urls import path
from  .views import list_obdrillingsummary, create_obdrillingsummary, update_obdrillingsummary, delete_obdrillingsummary

app_name = 'obdrillingsummary'

urlpatterns = [
    path('', list_obdrillingsummary, name='list_obdrillingsummary'),   
    path('create/', create_obdrillingsummary, name='create_obdrillingsummary'),
    path('<int:id>/update/', update_obdrillingsummary, name='update_obdrillingsummary'),
    path('<int:id>/delete/',delete_obdrillingsummary, name='delete_obdrillingsummary'), 
]