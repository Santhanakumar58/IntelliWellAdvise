from django.urls import path
from .views import  list_gpgradientsurvey, create_gpgradientsurvey,update_gpgradientsurvey, delete_gpgradientsurvey

app_name = 'gpgradientsurveys'

urlpatterns = [ 
    path('', list_gpgradientsurvey, name='list_gpgradientsurvey'),    
    path('create/', create_gpgradientsurvey, name='create_gpgradientsurvey'),
    path('<int:id>/update/', update_gpgradientsurvey, name='update_gpgradientsurvey'),   
    path('<int:id>/delete/', delete_gpgradientsurvey, name='delete_gpgradientsurvey'),
   ]