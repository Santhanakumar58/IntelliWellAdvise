from django.urls import path
from gpcementbondlogs.views import list_gpcementbondlog, create_gpcementbondlog, update_gpcementbondlog,delete_gpcementbondlog
app_name = 'gpcementbondlogs'

urlpatterns = [  
    path('<int:id>', list_gpcementbondlog, name='list_gpcementbondlog'),
    path('<int:id>/create/', create_gpcementbondlog, name='create_gpcementbondlog'),
    path('<int:id>/update/', update_gpcementbondlog, name='update_gpcementbondlog'),    
    path('<int:id>/delete/',delete_gpcementbondlog, name='delete_gpcementbondlog')
]