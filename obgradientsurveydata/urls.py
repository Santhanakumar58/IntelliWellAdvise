from distutils.command.upload import upload
from django.urls import path
from .views import  list_obgradientsurveydata, create_obgradientsurveydata,update_obgradientsurveydata, delete_obgradientsurveydata, excel_upload

app_name = 'obgradientsurveydata'

urlpatterns = [ 
    path('<int:id>', list_obgradientsurveydata, name='list_obgradientsurveydata'),    
    path('<int:id>/create/', create_obgradientsurveydata, name='create_obgradientsurveydata'),
    path('<int:id>/update/', update_obgradientsurveydata, name='update_obgradientsurveydata'), 
    path('<int:id>/delete/', delete_obgradientsurveydata, name='delete_obgradientsurveydata'),  
    path('<int:id>/excel_upload/', excel_upload, name='excel_upload')    
   ]