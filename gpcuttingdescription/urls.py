from django.urls import path
from .views import list_gpcutting, create_gpcutting, update_gpcutting, delete_gpcutting

app_name = 'gpcuttingdescription'

urlpatterns = [  
    path('',list_gpcutting, name='list_gpcutting'),
    path('create/', create_gpcutting, name='create_gpcutting'),
    path('<int:id>/update/', update_gpcutting, name='update_gpcutting'),
    path('<int:id>/delete/', delete_gpcutting, name='delete_gpcutting'), 

]
    