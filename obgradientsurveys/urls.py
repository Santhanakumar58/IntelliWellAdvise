from django.urls import path
from .views import  list_obgradientsurvey, create_obgradientsurvey,update_obgradientsurvey, delete_obgradientsurvey

app_name = 'obgradientsurveys'

urlpatterns = [ 
    path('', list_obgradientsurvey, name='list_obgradientsurvey'),    
    path('create/', create_obgradientsurvey, name='create_obgradientsurvey'),
    path('<int:id>/update/', update_obgradientsurvey, name='update_obgradientsurvey'),   
    path('<int:id>/delete/', delete_obgradientsurvey, name='delete_obgradientsurvey'),
   ]