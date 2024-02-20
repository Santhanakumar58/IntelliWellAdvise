from django.urls import path
from gicementbondlogs.views import list_gicementbondlog, create_gicementbondlog, update_gicementbondlog,delete_gicementbondlog
app_name = 'gicementbondlogs'

urlpatterns = [  
    path('<int:id>', list_gicementbondlog, name='list_gicementbondlog'),
    path('<int:id>/create/', create_gicementbondlog, name='create_gicementbondlog'),
    path('<int:id>/update/', update_gicementbondlog, name='update_gicementbondlog'),    
    path('<int:id>/delete/',delete_gicementbondlog, name='delete_gicementbondlog')
]