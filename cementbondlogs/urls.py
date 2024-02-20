from django.urls import path
from cementbondlogs.views import list_cementbondlog, create_cementbondlog, update_cementbondlog,delete_cementbondlog
app_name = 'cementbondlogs'

urlpatterns = [  
    path('<int:id>', list_cementbondlog, name='list_cementbondlog'),
    path('<int:id>/create/', create_cementbondlog, name='create_cementbondlog'),
    path('<int:id>/update/', update_cementbondlog, name='update_cementbondlog'),    
    path('<int:id>/delete/',delete_cementbondlog, name='delete_cementbondlog')
]