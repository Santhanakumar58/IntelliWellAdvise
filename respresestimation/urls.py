from django.urls import path
from .views import  list_respres, create_respres,update_respres, delete_respres

app_name = 'respresestimation'

urlpatterns = [ 
    path('', list_respres, name='list_respres'),    
    path('create/', create_respres, name='create_respres'),
    path('<int:id>/update/', update_respres, name='update_respres'),   
    path('<int:id>/delete/', delete_respres, name='delete_respres'),
]