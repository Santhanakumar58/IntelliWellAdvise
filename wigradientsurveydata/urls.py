from distutils.command.upload import upload
from django.urls import path
from .views import  list_wigradientsurveydata, create_wigradientsurveydata,update_wigradientsurveydata, delete_wigradientsurveydata, excel_upload

app_name = 'wigradientsurveydata'

urlpatterns = [ 
    path('<int:id>', list_wigradientsurveydata, name='list_wigradientsurveydata'),    
    path('<int:id>/create/', create_wigradientsurveydata, name='create_wigradientsurveydata'),
    path('<int:id>/update/', update_wigradientsurveydata, name='update_wigradientsurveydata'), 
    path('<int:id>/delete/', delete_wigradientsurveydata, name='delete_wigradientsurveydata'),  
    path('<int:id>/excel_upload/', excel_upload, name='excel_upload')    
   ]