from django.urls import path
from .views import  list_gigradientsurvey, create_gigradientsurvey,update_gigradientsurvey, delete_gigradientsurvey

app_name = 'gigradientsurveys'

urlpatterns = [ 
    path('', list_gigradientsurvey, name='list_gigradientsurvey'),    
    path('create/', create_gigradientsurvey, name='create_gigradientsurvey'),
    path('<int:id>/update/', update_gigradientsurvey, name='update_gigradientsurvey'),   
    path('<int:id>/delete/', delete_gigradientsurvey, name='delete_gigradientsurvey'),
   ]