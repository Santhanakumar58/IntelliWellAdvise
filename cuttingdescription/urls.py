from django.urls import path
from .views import list_cutting, create_cutting, update_cutting, delete_cutting

app_name = 'cuttingdescription'

urlpatterns = [  
    path('',list_cutting, name='list_cutting'),
    path('create/', create_cutting, name='create_cutting'),
    path('<int:id>/update/', update_cutting, name='update_cutting'),
    path('<int:id>/delete/', delete_cutting, name='delete_cutting'), 

]
    