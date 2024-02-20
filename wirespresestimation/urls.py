from django.urls import path
from .views import  list_wirespres, create_wirespres,update_wirespres, delete_wirespres

app_name = 'wirespresestimation'

urlpatterns = [ 
    path('', list_wirespres, name='list_wirespres'),    
    path('create/', create_wirespres, name='create_wirespres'),
    path('<int:id>/update/', update_wirespres, name='update_wirespres'),   
    path('<int:id>/delete/', delete_wirespres, name='delete_wirespres'),
]