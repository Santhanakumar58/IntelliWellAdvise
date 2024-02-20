from django.urls import path
from .views import  list_difflib, create_difflib,update_difflib, delete_difflib


app_name = 'differentialliberation'

urlpatterns = [ 
    path('', list_difflib, name='list_difflib'),    
    path('create/', create_difflib, name='create_difflib'),
    path('<int:id>/update/', update_difflib, name='update_difflib'),   
    path('<int:id>/delete/', delete_difflib, name='delete_difflib'),
   ]