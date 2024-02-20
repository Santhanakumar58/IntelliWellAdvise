from django.urls import path
from .views import list_gicutting, create_gicutting, update_gicutting, delete_gicutting

app_name = 'gicuttingdescription'

urlpatterns = [  
    path('',list_gicutting, name='list_gicutting'),
    path('create/', create_gicutting, name='create_gicutting'),
    path('<int:id>/update/', update_gicutting, name='update_gicutting'),
    path('<int:id>/delete/', delete_gicutting, name='delete_gicutting'), 

]
    