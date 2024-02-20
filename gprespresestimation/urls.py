from django.urls import path
from .views import  list_gprespres, create_gprespres,update_gprespres, delete_gprespres

app_name = 'gprespresestimation'

urlpatterns = [ 
    path('', list_gprespres, name='list_gprespres'),    
    path('create/', create_gprespres, name='create_gprespres'),
    path('<int:id>/update/', update_gprespres, name='update_gprespres'),   
    path('<int:id>/delete/', delete_gprespres, name='delete_gprespres'),
]