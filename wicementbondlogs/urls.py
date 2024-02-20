from django.urls import path
from wicementbondlogs.views import list_wicementbondlog, create_wicementbondlog, update_wicementbondlog,delete_wicementbondlog
app_name = 'wicementbondlogs'

urlpatterns = [  
    path('<int:id>', list_wicementbondlog, name='list_wicementbondlog'),
    path('<int:id>/create/', create_wicementbondlog, name='create_wicementbondlog'),
    path('<int:id>/update/', update_wicementbondlog, name='update_wicementbondlog'),    
    path('<int:id>/delete/',delete_wicementbondlog, name='delete_wicementbondlog')
]