from django.urls import path
from .views import  list_blackoilpvt, create_blackoilpvt,update_blackoilpvt, delete_blackoilpvt

app_name = 'blackoilpvt'

urlpatterns = [ 
    path('', list_blackoilpvt, name='list_blackoilpvt'),    
    path('create/', create_blackoilpvt, name='create_blackoilpvt'),
    path('<int:id>/update/', update_blackoilpvt, name='update_blackoilpvt'),   
    path('<int:id>/delete/', delete_blackoilpvt, name='delete_blackoilpvt'),
   ]