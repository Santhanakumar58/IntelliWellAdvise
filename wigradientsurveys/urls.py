from django.urls import path
from .views import  list_wigradientsurvey, create_wigradientsurvey,update_wigradientsurvey, delete_wigradientsurvey

app_name = 'wigradientsurveys'

urlpatterns = [ 
    path('', list_wigradientsurvey, name='list_wigradientsurvey'),    
    path('create/', create_wigradientsurvey, name='create_wigradientsurvey'),
    path('<int:id>/update/', update_wigradientsurvey, name='update_wigradientsurvey'),   
    path('<int:id>/delete/', delete_wigradientsurvey, name='delete_wigradientsurvey'),
   ]