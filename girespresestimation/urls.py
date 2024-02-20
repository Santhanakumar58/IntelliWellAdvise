from django.urls import path
from .views import  list_girespres, create_girespres,update_girespres, delete_girespres

app_name = 'girespresestimation'

urlpatterns = [ 
    path('', list_girespres, name='list_girespres'),    
    path('create/', create_girespres, name='create_girespres'),
    path('<int:id>/update/', update_girespres, name='update_girespres'),   
    path('<int:id>/delete/', delete_girespres, name='delete_girespres'),
]