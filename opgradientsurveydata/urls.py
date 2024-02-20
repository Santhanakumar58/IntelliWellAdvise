from distutils.command.upload import upload
from django.urls import path
from .views import  list_gradientsurveydata, create_gradientsurveydata,update_gradientsurveydata, delete_gradientsurveydata, excel_upload

app_name = 'opgradientsurveydata'

urlpatterns = [ 
    path('<int:id>', list_gradientsurveydata, name='list_gradientsurveydata'),    
    path('<int:id>/create/', create_gradientsurveydata, name='create_gradientsurveydata'),
    path('<int:id>/update/', update_gradientsurveydata, name='update_gradientsurveydata'), 
    path('<int:id>/delete/', delete_gradientsurveydata, name='delete_gradientsurveydata'),  
    path('<int:id>/excel_upload/', excel_upload, name='excel_upload')    
   ]