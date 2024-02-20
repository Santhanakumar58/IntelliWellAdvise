from distutils.command.upload import upload
from django.urls import path
from .views import  list_gigradientsurveydata, create_gigradientsurveydata,update_gigradientsurveydata, delete_gigradientsurveydata, excel_upload

app_name = 'gigradientsurveydata'

urlpatterns = [ 
    path('<int:id>', list_gigradientsurveydata, name='list_gigradientsurveydata'),    
    path('<int:id>/create/', create_gigradientsurveydata, name='create_gigradientsurveydata'),
    path('<int:id>/update/', update_gigradientsurveydata, name='update_gigradientsurveydata'), 
    path('<int:id>/delete/', delete_gigradientsurveydata, name='delete_gigradientsurveydata'),  
    path('<int:id>/excel_upload/', excel_upload, name='excel_upload')    
   ]