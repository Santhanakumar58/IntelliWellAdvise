from django.urls import path
from .views import  list_gradientsurvey, create_gradientsurvey,update_gradientsurvey, delete_gradientsurvey

app_name = 'opgradientsurveys'

urlpatterns = [ 
    path('', list_gradientsurvey, name='list_gradientsurvey'),    
    path('create/', create_gradientsurvey, name='create_gradientsurvey'),
    path('<int:id>/update/', update_gradientsurvey, name='update_gradientsurvey'),   
    path('<int:id>/delete/', delete_gradientsurvey, name='delete_gradientsurvey'),
   ]