from django.urls import path
from  .views import list_drillingsummary, create_drillingsummary, update_drillingsummary, delete_drillingsummary

app_name = 'drillingsummary'

urlpatterns = [
    path('', list_drillingsummary, name='list_drillingsummary'),   
    path('create/', create_drillingsummary, name='create_drillingsummary'),
    path('<int:id>/update/', update_drillingsummary, name='update_drillingsummary'),
    path('<int:id>/delete/',delete_drillingsummary, name='delete_drillingsummary'), 
]