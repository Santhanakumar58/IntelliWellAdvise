from django.urls import path
from obcementbondlogs.views import list_obcementbondlog, create_obcementbondlog, update_obcementbondlog,delete_obcementbondlog
app_name = 'obcementbondlogs'

urlpatterns = [  
    path('<int:id>', list_obcementbondlog, name='list_obcementbondlog'),
    path('<int:id>/create/', create_obcementbondlog, name='create_obcementbondlog'),
    path('<int:id>/update/', update_obcementbondlog, name='update_obcementbondlog'),    
    path('<int:id>/delete/',delete_obcementbondlog, name='delete_obcementbondlog')
]