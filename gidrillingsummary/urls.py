from django.urls import path
from  .views import list_gidrillingsummary, create_gidrillingsummary, update_gidrillingsummary, delete_gidrillingsummary

app_name = 'gidrillingsummary'

urlpatterns = [
    path('', list_gidrillingsummary, name='list_gidrillingsummary'),   
    path('create/', create_gidrillingsummary, name='create_gidrillingsummary'),
    path('<int:id>/update/', update_gidrillingsummary, name='update_gidrillingsummary'),
    path('<int:id>/delete/',delete_gidrillingsummary, name='delete_gidrillingsummary'), 
]