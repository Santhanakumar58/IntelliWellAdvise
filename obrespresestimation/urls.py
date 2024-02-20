from django.urls import path
from .views import  list_obrespres, create_obrespres,update_obrespres, delete_obrespres

app_name = 'obrespresestimation'

urlpatterns = [ 
    path('', list_obrespres, name='list_obrespres'),    
    path('create/', create_obrespres, name='create_obrespres'),
    path('<int:id>/update/', update_obrespres, name='update_obrespres'),   
    path('<int:id>/delete/', delete_obrespres, name='delete_obrespres'),
]