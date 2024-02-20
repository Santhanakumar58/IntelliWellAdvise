from distutils.command.upload import upload
from django.urls import path
from .views import  list_gpgradientsurveydata, create_gpgradientsurveydata,update_gpgradientsurveydata, delete_gpgradientsurveydata, excel_upload

app_name = 'gpgradientsurveydata'

urlpatterns = [ 
    path('<int:id>', list_gpgradientsurveydata, name='list_gpgradientsurveydata'),    
    path('<int:id>/create/', create_gpgradientsurveydata, name='create_gpgradientsurveydata'),
    path('<int:id>/update/', update_gpgradientsurveydata, name='update_gpgradientsurveydata'), 
    path('<int:id>/delete/', delete_gpgradientsurveydata, name='delete_gpgradientsurveydata'),  
    path('<int:id>/excel_upload/', excel_upload, name='excel_upload')    
   ]